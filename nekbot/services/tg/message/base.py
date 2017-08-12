


class MessageBaseMixin(object):
    def parse_update(self, update):
        self.user = None
        self.chat = None

