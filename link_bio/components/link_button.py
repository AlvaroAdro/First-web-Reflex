import reflex as rx
from link_bio.styles import styles

def link_button(title:str, body:str, image: str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width= styles.Size.BIG.value,
                    margin=styles.Size.SMALL.value,
                    alt=title
                ),
                rx.vstack(
                    rx.heading(title,
                               size="5",
                               style=styles.botton_title_style
                               ),
                    rx.text(body,
                            size="2",
                            style=styles.botton_body_style
                            ),
                    spacing="0"
                ),
                align="center",
                width="100%"   
            ),
            align="center",
            width="100%"
        ),
        href=url,
        is_external=True,
        width="100%"
    )