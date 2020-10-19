import logging

import click
from gevent.pywsgi import WSGIServer

from backend.cli.commands import commands, shared_options

logger = logging.getLogger(__name__)


@commands.command()
@shared_options
@click.option("--host", "-h", default="127.0.0.1", help="Where to listen")
@click.option("--port", "-p", default=45731, help="Port to listen on")
def start(host, port):
    """Start the backend."""
    from backend.tasks import huey, schedule_tasks
    from backend.web.app import create_app

    app = create_app()

    schedule_tasks()
    huey.start()

    server = WSGIServer((host, port), app)
    server.serve_forever()
