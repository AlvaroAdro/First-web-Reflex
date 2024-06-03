import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles

#class State(rx.State):
#    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.DEFAULT.value
            ),
        ),    
        footer()
    )

app = rx.App(
    stylsheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title= "Varodev | Aprende conmigo programacion y desarrolo de software.",
    description= "Hola, mi nombre es Alvaro Adrover. Soy aprendiz de software, estoy aprendiendo Python y desarrolo tanto web como de APP.",
    image= "Varo.svg"
    )
