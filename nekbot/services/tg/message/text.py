from nekbot.message.text import TextMessage
from nekbot.services.tg.message.base import MessageBaseMixin


class TelegramTextMessage(MessageBaseMixin, TextMessage):
    def parse_update(self, update):
        super(TelegramTextMessage, self).parse_update(update)

    def send(self):
        # TODO:
        recipient = self.message.message.chat.id
        self.bot.send_message(recipient, self.get_body())
