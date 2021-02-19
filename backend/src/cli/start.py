# This is really just a convenience command... for real production use we probably don't
# want to run this, as it doesn't restart any failed services. That's possibly something
# TODO, or not, since it is way better to just create systemd units or openrc whatevers
# for hypercorn and huey.

import time
from multiprocessing import Process

import click

from src.cli.commands import commands, shared_options
from src.services import start_task_queue, start_webserver


@commands.command()
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
