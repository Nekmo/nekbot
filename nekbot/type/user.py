

class User(object):
    def __init__(self, data):
        self.data = data

    @property
    def id(self):
        return self.get_id()

    def get_id(self):
        raise NotImplementedError

    @property
    def name(self):
        return self.get_name()

    def get_name(self):
        raise NotImplementedError


class ChatMember(object):
    def __init__(self, data):
        self.data = data

    @property
    def id(self):
        return self.get_id()

    def get_id(self):
        raise NotImplementedError

    @property
    def name(self):
        return self.get_name()

    def get_name(self):
        raise NotImplementedError
