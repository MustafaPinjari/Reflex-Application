import reflex as rx
from reflex_gpt import navigation
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def base_navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="40px",
                        border_radius="25%",
                    ),
                    rx.heading(
                            "ReflexGpt",
                            size="7",
                            weight="bold",
                        ),
                        align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_US_ROUTE),
                    navbar_link("Chat",navigation.routes.CHAT_ROUTE),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
                border_radius="40%",
            ),
            border_radius="40%",
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="40px",
                        border_radius="25%",
                    ),
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=navigation.state.NavState.to_home),
                        rx.menu.item("About", on_click=navigation.state.NavState.to_about_us),
                        rx.menu.item("Chat", on_click= navigation.state.NavState.to_chat)
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="2em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        border_radius="2em",
    )