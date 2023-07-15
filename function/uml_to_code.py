import json
from function.gpt import GPTInstance

def generate_dir_from_uml(uml: str) -> object:
    """Given a UML string, queries the chatbot for a JSON representation of
    the associated file directory.
    """
    FALLBACK_ERROR_MESSAGE = {
        "url": None,
        "comments": "I'm afraid I cannot generate a file directory at the moment. Please try again",
    }

    codegen_agent = GPTInstance(
        system_prompt="Given a UML diagram and problem description, generate the folder structure for the repo to implement it",
        functions=[
            {
                "name": "submit_folder_structure",
                "description": "Submit the the folder structure associated with the project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "folder_structure": {
                            "type": "string",
                            "description": "JSON String where each folder is a key and values might be other dictionaries or strings if a file",
                        },
                    },
                    "required": ["folder_structure"],
                },
            }
        ],
    )
    output = codegen_agent(
        f"Provide a full file directoy containing python files that implement the following UML: {uml}. Only provide the file directory. Do not explain. Do not give anything else."
    )

    # print(output)

    function_call = output.get("function_call", None)

    if function_call is None:
        return None

    if function_call["name"] != "submit_folder_structure":
        return None
    else:
        arguments = function_call["arguments"]
        arguments = json.loads(arguments)

    return arguments
