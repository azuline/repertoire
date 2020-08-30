import json

from voluptuous import Invalid

SORT_OPTIONS = {
    "recentlyAdded": "rls.added_on",
    "title": "rls.title",
    "year": "rls.release_year",
    "random": "RANDOM()",
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
            raise Invalid

        if not isinstance(list_, list):
            raise Invalid

        return [schema(v) for v in list_]

    return validator
