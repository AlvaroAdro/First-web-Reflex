import reflex as rx
import datetime
import link_bio.styles.styles as styles
from ..styles.color import color as color
from ..variables import constantes as const

def footer() -> rx.Component:
    return rx.center(
            rx.vstack(
            rx.image(src="Varodev.svg",
                     align="center",
                     height="auto",
                     width="10em",
                     ),
            rx.link(f"2024 - {datetime.date.today().year} Varodev By Alvaro Adrover v1.",
                href=const.INSTAGRAM_URL,
                is_external=True,
                size="3",
                color=styles.text_color.TITLE.value,
                _hover={
                    "color":styles.color.HOVER.value
                }
            ),
            rx.text("BUILDING SOFTWARE WITH <3 FROM ALICANTE TO THE WORLD.",
                    size="4"
                ),
                padding=styles.Size.BIG.value,
                width="100%"
        ),
        align="center",
        justify="center",
        color=styles.text_color.BODY.value,
        as_child=True,
        spacing="4",
        padding= styles.Size.BIGGEST.value
    )