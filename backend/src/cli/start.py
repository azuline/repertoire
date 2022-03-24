import time
from multiprocessing import Process

import click

from src.cli.commands import commands, migrate, shared_options
from src.services import start_task_queue, start_webserver


@commands.command()
@migrate
@shared_options
@click.option("--host", "-h", default="127.0.0.1", help="Where to listen")
@click.option("--port", "-p", default=45731, help="Port to listen on")
@click.option("--workers", "-p", default=1, help="Number of task queue workers")
def start(host: str, port: int, workers: int):
    """Start the backend services."""
    webserver = dict(target=start_webserver, args=(host, port))
    queue = dict(target=start_task_queue, args=(workers,))

    processes = [
        (webserver, Process(**webserver)),  # type: ignore
        (queue, Process(**queue)),  # type: ignore
    ]

    for _, p in processes:
        p.start()

    # Restart on failure.
    while True:
        for i, (args, p) in enumerate(processes):
            if p.is_alive():
                continue

            new_p = Process(**args)  # type: ignore
            new_p.start()
            processes[i] = (args, new_p)

        time.sleep(0.1)
