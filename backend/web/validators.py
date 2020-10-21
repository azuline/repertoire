from voluptuous import Invalid


def StringBool(value):
    if value == "true":
        return True
    elif value == "false":
        return False
    raise Invalid(f"Expected 'true' or 'false', not '{value}'")
