from voluptuous import Invalid


def StringBool(value: str) -> bool:
    """
    Given a string "true" or "false", return the associated boolean.

    :param value: The string to convert!
    :return: The converted boolean.
    """
    if value == "true":
        return True
    elif value == "false":
        return False
    raise Invalid(f"Expected 'true' or 'false', not '{value}'")
