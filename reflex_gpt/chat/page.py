import reflex as rx
from reflex_gpt import base_layout
from .form import chat_form

def chat_page() -> rx.Component:
    return base_layout(
        rx.vstack(
            rx.heading("Chat Here", size="9"),
            chat_form(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

