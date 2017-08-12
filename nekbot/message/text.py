import emoji as emoji

from nekbot.message.base import MessageBase


class TextMessage(MessageBase):
    message_class = 'TextMessage'
    emoji_mode = True
    format_mode = True
    safe_html = False
    body = ''

    def get_args(self):
        return self.context

    def get_body(self, body=''):
        body = body or self.body
        if self.format_mode:
            body = body.format(self.get_args())
        if self.emoji_mode:
            body = emoji.emojize(body, use_aliases=True)
        return body
