from typing import Dict

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.library import collection

gql_top_genre = ObjectType("TopGenre")


@gql_top_genre.field("genre")
def resolve_artist(obj: Dict, info: GraphQLResolveInfo) -> collection.T:
    return obj["genre"]


@gql_top_genre.field("numMatches")
def resolve_role(obj: Dict, info: GraphQLResolveInfo) -> int:
    return obj["num_matches"]
