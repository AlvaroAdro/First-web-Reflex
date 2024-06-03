import reflex as rx
from enum import Enum
from .color import color as color
from .color import text_color as text_color
from .fonts import font as font

MAX_WIDTH="600px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap",
    "https://fonts.googleapis.com/css2?family=DmSerifDisplay&display=swap"
]


class Size(Enum):
    SMALLER= "0.3em"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"
    BIGGEST= "2.5em"


BASE_STYLE = {
    "background_color": color.BACKGROUND.value,
    "font_family": font.DEFAULT.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "text_align": "start",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": color.CONTENT.value,
        "_hover": {
            "background_color": color.HOVER.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {},
    }
}


botton_title_style= dict(
    color=text_color.TITLE
    
)



botton_body_style= dict(
    color=text_color.BODY
    
)

title_style= dict(
    align="center",
    padding_top=Size.DEFAULT.value,
    color=text_color.TITLE.value
)


navbar_title_style= dict(
    align="center",
    color=color.PRIMARY.value,
    font_family=font.LOGO.value
)