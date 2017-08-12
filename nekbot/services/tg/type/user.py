from nekbot.type.user import User


class TelegramUser(User):
    def get_id(self):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError
