from dataclasses import dataclass

from ariadne import ObjectType

from backend.enums import GraphQLError

gql_error = ObjectType("Error")


@dataclass
class Error:
    """A dataclass to represent the GraphQL Error type."""

    #:
    error: GraphQLError
    #:
    message: str
