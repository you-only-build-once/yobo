import json

from function.gpt import GPTInstance
from function.gpt4_examples import folder_examples
import os


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

def download_folder_structure(folder_dir:json):
    for key in folder_dir:
        if isinstance(folder_dir[key], dict):
            if len(folder_dir[key]) == 0:
                with open(key, 'w') as fp:
                    continue
            else:
                os.mkdir(key)
            os.chdir(key)
            download_folder_structure(folder_dir[key])
            os.chdir('..')
        else:
            os.mkdir(folder_dir[key])