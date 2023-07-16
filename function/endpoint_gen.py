import json

from function.gpt import GPTInstance
from function.gpt4_examples import endpoint_examples


def endpoint_generation(
    problem_description: str,
    uml_code: str,
    folder_structure: dict,
    max_retries: int = 3,
):
    FALLBACK_ERROR_MESSAGE = {
        "comments": "I'm afraid I cannot generate a file directory at the moment. Please try again",
    }

    endpoint_agent = GPTInstance(
        system_prompt="You are a helpful assistant.",
        functions=[
            {
                "name": "submit_endpoints",
                "description": "Submit the endpoints needed for the project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "endpoints": {
                            "type": "string",
                            "description": "JSON String containing all the endpoints",
                        },
                    },
                    "required": ["endpoints"],
                },
            }
        ],
    )

    endpoint_agent.messages += endpoint_examples

    retries = 0

    while retries < max_retries:
        try:
            output = endpoint_agent(
                "With the following information, tell me which endpoints should be implemented in each file (be specific and use type hints), and explain the relationships between them."
                f"The problem is {problem_description}.\n"
                f"The architecture diagram is as follows: {uml_code}\n"
                f"And this is the file structure:\n{folder_structure}"
            )

            print(output)

            function_call = output.get("function_call", None)

            if function_call is None:
                retries += 1
                endpoint_agent.logger.warning(
                    "ChatGPT response unsuficient (No function call). Retrying..."
                )
                continue

            if function_call["name"] != "submit_endpoints":
                retries += 1
                endpoint_agent.logger.warning(
                    "ChatGPT response unsuficient (Wrong function). Retrying..."
                )
                continue
            else:
                arguments = function_call["arguments"]
                arguments = json.loads(arguments)

                return arguments
        except json.JSONDecodeError as e:
            retries += 1
            endpoint_agent.logger.warning(
                "ChatGPT response unsuficient (JSON Error). Retrying..."
            )
            pass

    return FALLBACK_ERROR_MESSAGE
