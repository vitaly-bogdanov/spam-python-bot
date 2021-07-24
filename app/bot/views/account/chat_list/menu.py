from aiogram.types import InputFile

from bot.models.file import ChatsFile
from bot.views.account.chat_list.keyboards import get_chat_list_keyboard


class ChatListMenu:
    def __init__(self, state):
        self.state = state
        self.document = ChatsFile(state.get('type'))

    def get_text(self):
        return f"База чатов {self.state.get('alias')}-аккаунта на данный момент."

    def get_keyboard(self):
        return get_chat_list_keyboard(self.state)

    def get_document(self):
        return InputFile(self.document.get_file())
