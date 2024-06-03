import reflex as rx
import link_bio.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(src="Varodev.svg",
                 width= "6em",
                 align= "start",
                 alt= "Logo de Varodev"
        ),
        position="sticky",
        bg=styles.color.CONTENT.value,
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.SMALL.value,
        z_index="999",
        top="0"
    )