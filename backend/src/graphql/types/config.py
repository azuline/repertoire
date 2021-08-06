from pathlib import Path
from typing import Any, Optional

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src import config
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.tasks.periodic import reschedule_indexer

gql_config = ObjectType("Config")


@query.field("config")
def resolve_config(_obj: Any, _info: GraphQLResolveInfo) -> dict:
    return _get_config()


@mutation.field("updateConfig")
def resolve_update_config(
    _obj: Any,
    info: GraphQLResolveInfo,
    musicDirectories: Optional[list[str]] = None,
    indexCrontab: Optional[str] = None,
) -> dict:

    if musicDirectories:
        config.set_music_directories(musicDirectories, info.context.db)
    if indexCrontab:
        config.set_index_crontab(indexCrontab, info.context.db)
    info.context.db.commit()

    reschedule_indexer()
    return _get_config()


def _get_config() -> dict:
    music_directories = [
        dict(directory=d, exists_on_disk=Path(d).is_dir())
        for d in config.music_directories()
    ]

    return dict(
        music_directories=music_directories,
        index_crontab=config.index_crontab_str(),
    )
