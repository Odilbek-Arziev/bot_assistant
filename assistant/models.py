from botmother.models import AbstractChat


class Chat(AbstractChat):
    class Meta(AbstractChat.Meta):
        db_table = 'assistant_chats'
