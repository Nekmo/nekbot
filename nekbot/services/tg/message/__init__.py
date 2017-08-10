from nekbot.services.tg.message.text import TextMessageMixin
from nekbot.utils.modules import import_string

__all__ = ['TextMessageMixin']

def get_message_cls(msg_cls):
    """Apply Telegram Message Mixin to NekBot Message class. 
    :param msg_cls: 
    :return: 
    """
    mixin_class = msg_cls.mixin_class
    mixin = import_string('nekbot.services.tg.message.{}'.format(mixin_class))

    class Message(mixin, msg_cls):
        pass
    return Message


def parse_telegram_update(update):
    """Translate Telegram update to Nekmo class
    """
    # TODO:
    return update
