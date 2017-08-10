


class MessageBaseMixin(object):
    bot = None
    message = None

    def send(self):
        raise NotImplementedError
