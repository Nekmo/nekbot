from nekbot.handler.command import CommandHandler

def register(*handlers):
    def wrapper(fn):
        return fn
    return wrapper
