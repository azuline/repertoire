from typing import Dict

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.library import collection

top_genre_resolver = ObjectType("TopGenre")


@top_genre_resolver.field("genre")
def resolve_artist(obj: Dict, info: GraphQLResolveInfo) -> collection.T:
    return obj["genre"]


@top_genre_resolver.field("numMatches")
def resolve_role(obj: Dict, info: GraphQLResolveInfo) -> int:
    return obj["num_matches"]
