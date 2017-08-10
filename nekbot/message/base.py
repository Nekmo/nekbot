


class MessageBase(object):
    def __init__(self, bot, message, context=None):
        self.bot = bot
        self.message = message
        self.context = context or {}

    def send(self):
        raise NotImplementedError
