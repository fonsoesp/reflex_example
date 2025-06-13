"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    nombre: str = "Reflex"

    def cambiar_nombre(self, nuevo_nombre: str):
        """Change the name to greet."""
        self.nombre = nuevo_nombre


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(f"¡Hola, {State.nombre}!", size="9"),
            rx.input(
                placeholder="Escribe tu nombre",
                on_change=State.cambiar_nombre,
                value=State.nombre,
            ),
            spacing="4",
            padding="10",
            border_radius="lg",
            box_shadow="lg",
            justify="center",
            min_height="100vh",
        ),
        position="relative",
    )

    # Welcome Page (Index)
    # return rx.container(
    #     rx.color_mode.button(position="top-right"),
    #     rx.vstack(
    #         rx.heading("Welcome to Reflex!", size="9"),
    #         rx.text(
    #             "Get started by editing ",
    #             rx.code(f"{config.app_name}/{config.app_name}.py"),
    #             size="5",
    #         ),
    #         rx.link(
    #             rx.button("Check out our docs!"),
    #             href="https://reflex.dev/docs/getting-started/introduction/",
    #             is_external=True,
    #         ),
    #         spacing="5",
    #         justify="center",
    #         min_height="85vh",
    #     ),
    #     rx.logo(),
    # )


app = rx.App()
app.add_page(index)
