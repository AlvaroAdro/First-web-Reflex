import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import text_color as text_color
from link_bio.styles.fonts import font as font
from link_bio.styles.styles import color as color
from ...variables import constantes as const
from ...styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src="varo.jpg",
                    size="6",
                    radius="full",
                    background_color= color.CONTENT.value,
                    padding= Size.SMALLER.value
            ),
                rx.vstack(
                rx.heading("Alvaro Adrover",
                           size="5",
                           font_family= font.DEFAULT.value,
                           weight="bold"),
                rx.text("@Varodev"),
                    rx.hstack(
                        link_icon(
                            "icons/github.svg",
                            const.GITHUB_URL,
                            "icono de Github"),
                        link_icon(
                            "icons/google.svg",
                            const.INSTAGRAM_URL,
                            "icono de Google"),
                        link_icon(
                            "icons/linkedin-in.svg",
                            const.LINKEDIN_URL,
                            "icono de Linkedin")
                    )
                ),
                spacing="4"  
        ),
        rx.flex(
            info_text("+1", "años de experiencia"),
            rx.spacer(),
            info_text("+1", "Proyectos creados"),
            width="100%"
        ),  
        rx.text("""Soy un programador junior que esta empezando
                a programar y este es mi primer proyecto
                una web en la que dejar todos mis links en 
                los que poder contactarme a mi o a mi comunidad
                y crecer en el mundo tech que tanto nos 
                apasiona 💪​"""),
        size="4",
        align_items="center",
        color=text_color.BODY.value,
        spacing="6",
        padding= Size.SMALL.value
    )