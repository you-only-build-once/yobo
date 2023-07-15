import os
import logging
from typing import Optional, List, Dict

import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = os.environ.get("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")


class GPTInstance:
    def __init__(
        self,
        system_prompt: str = "You are a helpful assistant.",
        model="gpt-3.5-turbo",
        keep_state: bool = True,
        temperature: float = 1,
        logger_name: str = __name__,
        functions: Optional[List] = None,
    ):
        self.model = model
        self.messages = [{"role": "system", "content": system_prompt}]
        self.keep_state = keep_state
        self.temperature = temperature
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        self.functions = functions

    def __call__(
        self, input: Optional[str] = None, role: str = "user", *args, **kwargs
    ) -> Dict:

        history = [*self.messages]

        if input:
            history.append({"role": role, "content": input})

        functions = kwargs.pop("functions", self.functions)

        output = openai.ChatCompletion.create(
            model=self.model, messages=history, functions=functions, *args, **kwargs
        )
        output = output.choices[0].message

        self.logger.info(output)

        if self.keep_state:
            self.messages.append(output)

        return output
