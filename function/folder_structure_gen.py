import json

from function.gpt import GPTInstance
from function.gpt4_examples import folder_examples
import os
import zipfile
import io



def folder_structure_gen(problem_description: str, uml_code: str, max_retries: int = 3) -> str:
    FALLBACK_ERROR_MESSAGE = {
        "url": None,
        "comments": "I'm afraid I cannot generate a file directory at the moment. Please try again",
    }

    codegen_agent = GPTInstance(
        system_prompt="You are a helpful assistant.",
        functions=[
            {
                "name": "submit_file_structure",
                "description": "Submit the the folder structure associated with the project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_structure": {
                            "type": "string",
                            "description": "JSON String containing all the folders and files",
                        },
                    },
                    "required": ["file_structure"],
                },
            }
        ],
    )

    codegen_agent.messages += folder_examples

    retries = 0

    while retries < max_retries:
        try:
            output = codegen_agent(
                f"Help me come up with the organization for the code repository of my project.\nThe problem is {problem_description}.\n"
                f"The architecture diagram is as follows: {uml_code}"
            )

            print(output)

            function_call = output.get("function_call", None)

            if function_call is None:
                retries += 1
                codegen_agent.logger.warning("ChatGPT response unsuficient. Retrying...")
                continue

            if function_call["name"] != "submit_file_structure":
                retries += 1
                codegen_agent.logger.warning("ChatGPT response unsuficient. Retrying...")
                continue
            else:
                arguments = function_call["arguments"]
                out_folder = json.loads(arguments)
                folder_structure = out_folder["file_structure"]
                return folder_structure
        except json.JSONDecodeError as e:
            retries += 1
            codegen_agent.logger.warning("ChatGPT response unsuficient. Retrying...")
            pass

    return FALLBACK_ERROR_MESSAGE

def download_repo(endpoints: dict):
    """
    Params
        endpoints: list of dicts, each with keys "file_path" and "contents" containing
                   the relative path of the endpoint and the source code, respectively
    Returns:
        buffer: a BytesIO object containing all the endpoints.
    """
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_STORED) as zipf:
        for elem in endpoints:
            zipf.writestr(elem['file_path'], elem['contents'])
    return buffer
