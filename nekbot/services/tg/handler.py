from nekbot.handler.command import CommandHandler
from telegram.ext.commandhandler import CommandHandler as TgCommandHandler


def command_handler(fn, hl):
    return TgCommandHandler(hl.command, fn, allow_edited=hl.allow_edited, pass_args=hl.pass_args)


TELEGRAM_HANDLERS = {
    CommandHandler: command_handler,
}
