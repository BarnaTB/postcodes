from postcodes.utils.exceptions import CustomAPIException


def validate_fields(required_keys: tuple, dict_keys: tuple) -> bool:
    """Utility function to validate that a dictionary has all the required keys
    in the required order

    Args:
        required_keys[tuple]: A tuple of the required keys
        dict_keys[dict]: Dictionary to validate
    """
    return True if required_keys == dict_keys else False

def validate_response(response):
    """Utility function to validate that a response object has errors
    """
    if response.get("error"):
        raise CustomAPIException(status_code=response.get("status"), message=response.get("error"))
