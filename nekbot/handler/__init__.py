from collections import defaultdict

from nekbot.handler.command import CommandHandler


HANDLERS = defaultdict(list)


class HandlerStanza(object):
    def __init__(self, fn, *handlers):
        self.fn = fn
        self.handlers = handlers


class HandlerRegister(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, *handlers):
        def wrapper(fn):
            HANDLERS[self.app].append(HandlerStanza(fn, *handlers))
            return fn
        return wrapper
