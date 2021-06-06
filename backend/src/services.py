"""
This module contains functions that run repertoire's backend services.

The services are:
- The webserver
- The task queue
"""

import asyncio

from huey.consumer_options import ConsumerConfig
from hypercorn.asyncio import serve
from hypercorn.config import Config

from src.tasks.hueyy import huey
from src.tasks.periodic import schedule_tasks
from src.webserver.app import create_app


def start_webserver(host: int, port: int) -> None:
    """Start the Quart webserver."""
    config = Config()
    config.bind = [f"{host}:{port}"]

    app = create_app()
    asyncio.run(serve(app, config))  # type: ignore


def start_task_queue(num_workers: int) -> None:
    """Start the Huey task queue."""
    schedule_tasks()

    config = ConsumerConfig(workers=num_workers)
    consumer = huey.create_consumer(**config.values)
    consumer.run()
