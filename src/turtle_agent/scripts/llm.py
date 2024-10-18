#  Copyright (c) 2024. Jet Propulsion Laboratory. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from langchain_mistralai import ChatMistralAI


def get_llm(streaming: bool = False): 
    llm = ChatMistralAI(
        model_name="mistral-large-latest",
        temperature=0.0,
        max_retries=2,
        api_key=get_env_variable("MISTRAL_API_KEY"),
        max_concurrent_requests=1,
        streaming=streaming,
    )

    return llm


def get_env_variable(var_name: str) -> str:
    """
    Retrieves the value of the specified environment variable.

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the environment variable.

    Raises:
        ValueError: If the environment variable is not set.

    This function provides a consistent and safe way to retrieve environment variables.
    By using this function, we ensure that all required environment variables are present
    before proceeding with any operations. If a variable is not set, the function will
    raise a ValueError, making it easier to debug configuration issues.
    """
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable {var_name} is not set.")
    return value
