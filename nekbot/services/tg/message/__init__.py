from nekbot.services.tg.message.text import TextMessageMixin
from nekbot.utils.modules import import_string

__all__ = ['TextMessageMixin']

def get_message_cls(msg_cls):
    """Apply Telegram Message Mixin to NekBot Message class. 
    :param msg_cls: 
    :return: 
    """
    mixin_name = '{}Mixin'.format(msg_cls.__name__)
    mixin = import_string('nekbot.services.tg.message.{}'.format(mixin_name))

    class Message(msg_cls, mixin):
        pass
    return Message

def parse_telegram_update(update):
    """Translate Telegram update to Nekmo class
    """
    pass