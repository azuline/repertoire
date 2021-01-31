# This is really just a convenience command... for real production use we probably don't
# want to run this, as it doesn't restart any failed services. That's possibly something
# TODO, or not, since it is way better to just create systemd units or openrc whatevers
# for hypercorn and huey.

import asyncio
import logging
from multiprocessing import Process

import click
from huey import SqliteHuey
from huey.consumer_options import ConsumerConfig
from hypercorn.asyncio import serve
from hypercorn.config import Config

from src.cli.commands import commands, shared_options
from src.constants import Constants

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
    from src.webserver.app import create_app

    config = Config()
    config.bind = [f"{host}:{port}"]

    app = create_app()

    asyncio.run(serve(app, config))


def _start_task_queue(workers: int) -> None:
    from src.tasks import schedule_tasks

    cons = Constants()

    queue = SqliteHuey(filename=cons.huey_path)
    schedule_tasks(queue)

    config = ConsumerConfig(workers=workers)
    consumer = queue.create_consumer(**config.values)

    consumer.run()
