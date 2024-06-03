import reflex as rx
import link_bio.styles.styles as styles
from ..styles.fonts import font as font

def title(text:str) -> rx.Component:
    return rx.heading(text,
                        style=styles.title_style,
                        font_family= font.DEFAULT.value,
                        size="6",
                        weight="bold"
                    )