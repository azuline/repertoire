import asyncio
import logging
from multiprocessing import Process

import click
from huey import SqliteHuey
from huey.consumer_options import ConsumerConfig
from hypercorn.asyncio import serve
from hypercorn.config import Config

from backend.cli.commands import commands, shared_options
from backend.constants import HUEY_PATH

logger = logging.getLogger(__name__)


@commands.command()
@shared_options
@click.option("--host", "-h", default="127.0.0.1", help="Where to listen")
@click.option("--port", "-p", default=45731, help="Port to listen on")
@click.option("--workers", "-p", default=1, help="Number of task queue workers")
def start(host: str, port: int, workers: int):
    """Start the backend."""
    queue = Process(target=_start_task_queue, args=(workers,))
    webserver = Process(target=_start_webserver, args=(host, port))

    queue.start()
    webserver.start()

    webserver.join()


def _start_webserver(host: int, port: int) -> None:
    from backend.webserver.app import create_app

    config = Config()
    config.bind = [f"{host}:{port}"]

    app = create_app()

    asyncio.run(serve(app, config))


def _start_task_queue(workers: int) -> None:
    from backend.tasks import schedule_tasks

    queue = SqliteHuey(filename=HUEY_PATH)
    schedule_tasks(queue)

    config = ConsumerConfig(workers=workers)
    consumer = queue.create_consumer(**config.values)

    consumer.run()
