from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.library import collection

gql_top_genre = ObjectType("TopGenre")


@gql_top_genre.field("genre")
def resolve_artist(obj: dict, info: GraphQLResolveInfo) -> collection.T:
    return obj["genre"]


@gql_top_genre.field("numMatches")
def resolve_role(obj: dict, info: GraphQLResolveInfo) -> int:
    return obj["num_matches"]
