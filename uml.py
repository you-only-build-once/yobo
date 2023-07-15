import json
from typing import Dict

from plantuml import PlantUML

from gpt import GPTInstance

PLANT_UML_SERVER: PlantUML = PlantUML(url="http://www.plantuml.com/plantuml/img/")


def process_uml_code(uml_code: str) -> str:
    return PLANT_UML_SERVER.get_url(uml_code)


def generate_uml_code(project_requirements: str) -> Dict:

    FALLBACK_ERROR_MESSAGE = {
        "url": None,
        "comments": "I'm afraid I cannot generate a diagram at the moment. Please try again",
    }

    uml_agent = GPTInstance(
        functions=[
            {
                "name": "submit_plantuml_code",
                "description": "Submit the plant UML code",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plantuml_code": {
                            "type": "string",
                            "description": "The plantUML code to submit",
                        },
                        "context_and_reasoning": {
                            "type": "string",
                            "description": "The context and reasoning necessary for the user to understand the UML",
                        },
                    },
                    "required": ["plantuml_code", "context_and_reasoning"],
                },
            }
        ]
    )
    output = uml_agent(
        f"""Hey chatGPT, I want to brainstorm for a new project, the idea is:\n{project_requirements}
        Can you create an initial diagram (using plantUML) of how I can build it?
        """
    )

    function_call = output.get("function_call", None)

    if function_call is None:
        return FALLBACK_ERROR_MESSAGE

    if function_call["name"] != "submit_plantuml_code":
        return FALLBACK_ERROR_MESSAGE
    else:
        arguments = function_call["arguments"]
        arguments = json.loads(arguments)

        uml_code = arguments["plantuml_code"]
        url = process_uml_code(uml_code)

        return {
            "url": url,
            "comments": arguments["context_and_reasoning"],
        }
