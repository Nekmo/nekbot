


class MessageBase(object):
    def __init__(self, bot, message=None, context=None):
        self.bot = bot
        self.message = message
        self.context = context or {}

    def parse_update(self, update):
        raise NotImplementedError

    def send(self):
        raise NotImplementedError
