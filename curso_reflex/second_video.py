import reflex as rx
from rxconfig import config

class State(rx.State):
    pass

class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, data: dict):
        """Handle form submission and store the data."""
        self.form_data = data
        return rx.window_alert("Form submitted successfully!")

def componentes() -> rx.Component:
    return rx.vstack(
        rx.text("Texto normal"),
        rx.heading("Esto es un encabezado!", size="3"),
        rx.markdown(
            """
            ## Esto es un encabezado de nivel 2

            - Lista
            - Con
            - Elementos

            [Enlace a Reflex](https://reflex.dev)
            """
        ),
        rx.code(
            "print('¡Hola, Reflex!')",
            language="python",
            style={"backgroundColor": "#f0f0f0", "padding": "10px", "borderRadius": "5px"},
        ),
        spacing="4",
    )

def formulario() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                ),
                rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )
