from importlib import import_module


class App(object):
    def __init__(self, bot):
        self.bot = bot

    def get_module_string(self):
        return '.'.join(self.__class__.__module__.split('.')[:-1])

    def init(self):
        self.register_handlers()

    def register_handlers(self):
        from nekbot.handler import HANDLERS
        mod_string = self.get_module_string()
        try:
            import_module('{}.handlers'.format(mod_string))
        except Exception:
            return
        if self.__class__ not in HANDLERS:
            return
        for hl in HANDLERS[self.__class__]:
            self.bot.register_handler_stanza(hl)