import os
import click

from nekbot.conf import settings as nekbot_settings
from nekbot.core.server import get_service_class

ENVIRONMENT_VARIABLE = "NEKBOT_SETTINGS_MODULE"


@click.group()
@click.option('--debug/--no-debug', default=None)
@click.option('--settings', default=os.environ.get(ENVIRONMENT_VARIABLE, ''))
@click.pass_context
def cli(ctx, debug, settings):
    nekbot_settings.configure(settings)
    if debug is not None:
        nekbot_settings.set('DEBUG', debug)


@cli.command()
@click.pass_context
def run(ctx):
    cls = get_service_class()
    cls().run()
