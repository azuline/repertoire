from typing import Any

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src import config
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.tasks.periodic import reschedule_indexer

gql_config = ObjectType("Config")


@query.field("config")
def resolve_config(_obj: Any, _info: GraphQLResolveInfo) -> dict:
    return {
        "musicDirectories": config.music_directories(),
        "indexCrontab": config.index_crontab(),
    }


@mutation.field("updateConfig")
def resolve_update_config(
    _obj: Any,
    info: GraphQLResolveInfo,
    musicDirectories: list[str],
    indexCrontab: str,
) -> dict:
    config.set_music_directories(musicDirectories, info.context.db)
    config.set_index_crontab(indexCrontab, info.context.db)

    info.context.db.commit()

    reschedule_indexer()

    return {
        "musicDirectories": musicDirectories,
        "indexCrontab": indexCrontab,
    }
