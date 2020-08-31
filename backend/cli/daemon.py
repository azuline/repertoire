import logging
import os
import sys
from signal import SIGKILL, SIGTERM

import click
from daemonize import Daemonize
from gevent.pywsgi import WSGIServer

from backend.cli.commands import commands, shared_options
from backend.constants import PID_PATH
from backend.errors import CliError

logger = logging.getLogger(__name__)


@commands.command()
@shared_options
@click.option("--host", "-h", default="127.0.0.1", help="Where to listen")
@click.option("--port", "-p", default=45731, help="Port to listen on")
@click.option(
    "--foreground",
    "-fg",
    default=False,
    is_flag=True,
    help="Run daemon in foreground",
)
def start(host, port, foreground):
    """Start the backend daemon."""

    def run_daemon():
        from gevent import monkey

        monkey.patch_all()

        from backend.tasks import huey
        from backend.web.app import create_app

        app = create_app()

        huey.start()

        server = WSGIServer((host, port), app)
        server.serve_forever()

    from backend import handler  # Logger handler.

    logger = logging.getLogger()
    keep_fds = [handler.stream.fileno()]

    # If we are running in the foreground, also pipe logs to stdout.
    if foreground:
        stream_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s:%(name)s - %(message)s"
        )
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        keep_fds.append(stream_handler.stream.fileno())

    daemon = Daemonize(
        app="repertoire",
        pid=PID_PATH,
        action=run_daemon,
        logger=logger,
        keep_fds=keep_fds,
        foreground=foreground,
    )
    daemon.start()


@commands.command()
@shared_options
@click.option("--force", "-f", default=False, is_flag=True, help="Force quit")
def stop(force):
    """Stop the backend daemon."""
    try:
        with PID_PATH.open() as pf:
            pid = int(pf.read())
            os.kill(pid, SIGTERM if not force else SIGKILL)
    except (ValueError, FileNotFoundError):
        raise CliError("Daemon is not running")


@commands.command()
@shared_options
def status():
    """Show the backend daemon status."""
    try:
        with PID_PATH.open() as pf:
            click.echo(f"Daemon is running with PID {pf.read()}.")
    except FileNotFoundError:
        raise CliError("Daemon is not running.")
