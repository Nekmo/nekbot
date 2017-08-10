from nekbot.services.tg.message.base import MessageBaseMixin


class TextMessageMixin(MessageBaseMixin):

    def send(self):
        # TODO:
        recipient = self.message.message.chat.id
        self.bot.send_message(recipient, self.get_body())
