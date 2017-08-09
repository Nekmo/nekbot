from nekbot.handler.base import Handler


class CommandHandler(Handler):
    def __init__(self, command, allow_edited=False, pass_args=False):
        # TODO: pass_args a True
        self.command = command
        self.allow_edited = allow_edited
        self.pass_args = pass_args


class MessageHandler(Handler):
    pass


class RegexHandler(Handler):
    pass
