def query_model(input:str) -> dict:
    """
    Given user input, return model response as dictionary.
    """
    return {
        "response": "You entered " + input
    }