import json

from voluptuous import Invalid

from backend.enums import ReleaseSort

SORT_OPTIONS = {
    "releaseYear": ReleaseSort.RELEASE_YEAR,
    "title": ReleaseSort.TITLE,
    "year": ReleaseSort.YEAR,
    "random": ReleaseSort.RANDOM,
}


def SortOption(value):
    try:
        return SORT_OPTIONS[value]
    except KeyError:
        raise ValueError


def JSONList(schema):
    def validator(value):
        try:
            list_ = json.loads(value)
        except json.decoder.JSONDecodeError:
            raise Invalid("Expected a JSON-encoded list.")

        if not isinstance(list_, list):
            raise Invalid("Expected a JSON-encoded list.")

        return [schema(v) for v in list_]

    return validator


def StringBool(value):
    if value == "true":
        return True
    elif value == "false":
        return False
    raise Invalid(f"Expected 'true' or 'false', not '{value}'")
