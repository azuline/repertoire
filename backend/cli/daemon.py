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

    # If we are running in the foreground, also pipe logs to stdout.
    if foreground:
        logger = logging.getLogger()
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s:%(name)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    def run_daemon():
        from backend.tasks import huey
        from backend.web.app import create_app

        app = create_app()
        huey.start()

        logger.info(f"Listening on http://{host}:{port}/")
        server = WSGIServer((host, port), app)
        server.serve_forever()

    daemon = Daemonize(
        app="repertoire",
        pid=PID_PATH,
        action=run_daemon,
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
        PID_PATH.unlink()
    except (ValueError, FileNotFoundError):
        raise CliError("Daemon is not running")


@commands.command()
@shared_options
def status():
    """Show the backend daemon status."""
    try:
        with PID_PATH.open() as pf:
            click.echo(f"Daemon is running with PID {pf.read()}")
    except FileNotFoundError:
        raise CliError("Daemon is not running.")
