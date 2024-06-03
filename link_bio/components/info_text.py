import reflex as rx
from ..styles.color import text_color as text_color

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.text.span(
            title,
            color=text_color.TITLE.value,
        ),
        f" {body}",
        size="2"
    )