import reflex as rx
from . import page

class ChatState(rx.State):
    def handle_submit(self, form_data:dict):
        print(form_data)