from telegram.ext import Updater

from nekbot.conf import settings
from nekbot.services.base.bot import BotBase
from nekbot.utils.modules import import_string


class TelegramBot(BotBase):
    def __init__(self):
        self.updater = Updater(settings.TELEGRAM_TOKEN)
        self.dispatcher = self.updater.dispatcher

    @property
    def apps(self):
        # TODO: debe devolver la clase de App
        return [import_string('{}.app'.format(app)) for app in settings.INSTALLED_APPS]

    def init_apps(self):
        for app in self.apps:
            # TODO:
            app


    def run(self):
        self.updater.start_polling()
