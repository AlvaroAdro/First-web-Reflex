import reflex as rx
from ...components.link_button import link_button
from link_bio.components.title import title
from ...variables import constantes as const
from link_bio.styles.styles import Size as Size

def links() -> rx.Component:
    return rx.vstack(
        title("ENLACES PARA LA COMUNIDAD"),
        link_button("Instagram",
                    "Este es mi instagram donde encontraras creaciones mias",
                    "icons/instagram.svg",
                    const.INSTAGRAM_URL,
                    ),
        link_button("Youtube",
                    "Aqui tienes mi canal de Youtube donde encontraras todos mis videos",
                    "icons/youtube.svg",
                    const.YOUTUBE_URL
                    ),
        link_button("Twitch",
                    "Aqui podras seguirme en todos mis directos y preguntar cualquier duda",
                    "icons/twitch.svg",
                    const.TWITCH_URL
                    ),
        link_button("Discord",
                    "Este es el lugar idioneo donde crecer junto a mi y mi comunidad",
                    "icons/discord.svg",
                    const.DISCORD_URL
                    ),
        title("TRABAJA CONMIGO"),
        link_button("Instagram",
                    "Este es mi instagram donde encontraras creaciones mias",
                    "icons/instagram.svg",
                    const.INSTAGRAM_URL
                    ),
        link_button("Youtube",
                    "Aqui tienes mi canal de Youtube donde encontraras todos mis videos",
                    "icons/youtube.svg",
                    const.YOUTUBE_URL
                    ),
        link_button("Twitch",
                    "Aqui podras seguirme en todos mis directos y preguntar cualquier duda",
                    "icons/twitch.svg",
                    const.TWITCH_URL
                    ),
        link_button("Discord",
                    "Este es el lugar idioneo donde crecer junto a mi y mi comunidad",
                    "icons/discord.svg",
                    const.DISCORD_URL
                    ),
        width="100%",
        spacing="4",
        padding= Size.DEFAULT.value
    )