from importlib import import_module

import inspect
from telegram.ext import Updater

from nekbot.apps import App
from nekbot.conf import settings
from nekbot.exceptions import ProgrammingError
from nekbot.message.base import MessageBase
from nekbot.services.base.bot import BotBase
from nekbot.services.tg.handler import TELEGRAM_HANDLERS
from nekbot.services.tg.message import get_message_cls, parse_telegram_update
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

    def execute_function_handler(self, fn):
        is_msg_cls = False
        if inspect.isclass(fn) and issubclass(fn, MessageBase):
            # Apply Telegram Mixin Class
            fn = get_message_cls(fn)
            is_msg_cls = True
        def wrapper(bot, update):
            # TODO:
            message = parse_telegram_update(update)
            instance = fn(bot, message)
            if is_msg_cls:
                instance.send()
        return wrapper

    def register_handler_stanza(self, handler_stanza):
        fn = handler_stanza.fn
        for hl in handler_stanza.handlers:
            tg_handler = TELEGRAM_HANDLERS[hl.__class__](self.execute_function_handler(fn), hl)
            self.dispatcher.add_handler(tg_handler)

    def run(self):
        self.init_apps()
        self.updater.start_polling()
