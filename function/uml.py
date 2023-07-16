import json
from typing import Dict


from plantuml import PlantUML


from function.gpt import GPTInstance
from function.gpt4_examples import uml_examples

PLANT_UML_SERVER: PlantUML = PlantUML(url="http://www.plantuml.com/plantuml/img/")


def process_uml_code(uml_code: str) -> str:
    return PLANT_UML_SERVER.get_url(uml_code)


def generate_uml_code(
    project_requirements: str, framework_requirements: str, max_retries: int = 3
) -> Dict:

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
    uml_agent.messages += uml_examples

    retries = 0

    while retries < max_retries:

        try:
            output = uml_agent(
                f"""Hey chatGPT, I want to brainstorm for a new project, the idea is:\n{project_requirements}.
                These are my rough framework requirements:\n{framework_requirements}
                Can you create an initial diagram (using plantUML) of how I can build it?
                """
            )

            function_call = output.get("function_call", None)

            if function_call is None:
                retries += 1
                uml_agent.logger.warning("ChatGPT response unsuficient. Retrying...")
                continue

            if function_call["name"] != "submit_plantuml_code":
                retries += 1
                uml_agent.logger.warning("ChatGPT response unsuficient. Retrying...")
                continue
            else:
                arguments = function_call["arguments"]
                arguments = json.loads(arguments)

                uml_code = arguments["plantuml_code"]
                url = process_uml_code(uml_code)

                return {
                    "url": url,
                    "uml_code": uml_code,
                    "comments": arguments["context_and_reasoning"],
                }

        except json.JSONDecodeError as e:
            retries += 1
            uml_agent.logger.warning("ChatGPT response unsuficient. Retrying...")
            pass

    return FALLBACK_ERROR_MESSAGE
