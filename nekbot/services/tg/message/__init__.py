from nekbot.services.tg.message.text import TelegramTextMessage
from nekbot.utils.modules import import_string

__all__ = ['TelegramTextMessage']


def get_message_cls(msg_cls):
    """Apply Telegram Message Mixin to NekBot Message class. 
    :param msg_cls: 
    :return: 
    """
    mixin_class = 'Telegram{}'.format(msg_cls.message_class)
    mixin = import_string('nekbot.services.tg.message.{}'.format(mixin_class))

    class Message(mixin, msg_cls):
        pass
    return Message


def parse_telegram_update(bot, update):
    """Translate Telegram update to Nekmo class
    """
    # TODO:
    if hasattr(update, 'message'):
        message = TelegramTextMessage(bot)
    message
    return update
