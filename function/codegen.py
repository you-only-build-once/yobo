import json

from function.gpt import GPTInstance


def codegen(uml_code: str) -> str:
    codegen_agent = GPTInstance(
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
        ]
    )
    output = codegen_agent(
        f"Here is the uml code generate a folder structure: {uml_code} and submit it"
    )

    print(output)

    function_call = output.get("function_call", None)

    if function_call is None:
        return None

    if function_call["name"] != "submit_folder_structure":
        return None
    else:
        arguments = function_call["arguments"]
        arguments = json.loads(arguments)

        return arguments
