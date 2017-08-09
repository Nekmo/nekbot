from importlib import import_module

from telegram.ext import Updater

from nekbot.apps import App
from nekbot.conf import settings
from nekbot.exceptions import ProgrammingError
from nekbot.services.base.bot import BotBase
from nekbot.services.tg.handler import TELEGRAM_HANDLERS
from nekbot.utils.modules import get_subclass_objects


def get_app(mod):
    classes = list(get_subclass_objects(mod, App))
    if not classes:
        raise ProgrammingError("Module {} does not have App class.")
    if len(classes) > 1:
        raise ProgrammingError("Module {} has too many App class.")
    return classes[0]


class TelegramBot(BotBase):
    _apps = None

    def __init__(self):
        self.updater = Updater(token=settings.TELEGRAM_TOKEN)
        self.dispatcher = self.updater.dispatcher

    @property
    def module_apps(self):
        return [import_module('{}.app'.format(app)) for app in settings.INSTALLED_APPS]

    @property
    def apps(self):
        if not self._apps:
            self._apps = [get_app(mod)(self) for mod in self.module_apps]
        return self._apps

    def init_apps(self):
        for app in self.apps:
            # TODO:
            app.init()

    def register_handler_stanza(self, handler_stanza):
        fn = handler_stanza.fn
        for hl in handler_stanza.handlers:
            tg_handler = TELEGRAM_HANDLERS[hl.__class__](fn, hl)
            self.dispatcher.add_handler(tg_handler)

    def run(self):
        self.init_apps()
        self.updater.start_polling()
