import reflex as rx
from reflex_gpt import base_layout


def about_us_page() -> rx.Component:
    # About us Page
    
    return base_layout(
       rx.vstack(
             rx.heading("Welcome to Reflex About !", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )