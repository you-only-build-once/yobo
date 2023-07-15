import json

from function.gpt import GPTInstance


def codegen(problem_descrption: str, uml_code: str, folder_structure: str) -> str:
    codegen_agent = GPTInstance(
        system_prompt="Given a UML diagram and problem description, generate the code for the repo to implement it",
        functions=[
            {
                "name": "codegen_repo",
                "description": "Generate code repo for the project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_files": {
                            "type": "string",
                            "description": "list of objects (files) with the keys, 'file_path' and 'contents' containing the code generated for each file",
                        },
                    },
                    "required": ["list_of_files"],
                },
            }
        ],
    )
    output = codegen_agent(
        f"Problem description:\n{problem_descrption}\n UML:\n{uml_code} with folder structure {folder_structure}"
    )

    print(output)

    function_call = output.get("function_call", None)

    if function_call is None:
        return None

    if function_call["name"] != "list_of_files":
        return None
    else:
        arguments = function_call["arguments"]
        arguments = json.loads(arguments)

        return arguments