"""
G3 Service "Informations" panel (ToS / Privacy Policy / FaQ).
Posted via /panel-info. Every button answers with an EPHEMERAL message, so
only the person who pressed it can see it. All URLs come from config.py
(INFO_PANEL_*).

Each button opens its section (ToS / Privacy / FaQ) via SECTION_BUILDERS.
"""
from __future__ import annotations

from typing import Callable

import discord
from emojis import emoji as _emoji
from discord import app_commands, ui
from discord.ext import commands

import config
from emojis import emoji
from utils.permissions import slash_is_ownership_only

SMALL = discord.SeparatorSpacing.small
INFO_ACCENT = 0x0091FF


def _e(key: str) -> str:
    return emoji("info", key)


def build_panel_view() -> ui.LayoutView:
    def btn(label: str, key: str, custom_id: str) -> ui.Button:
        return ui.Button(
            style=discord.ButtonStyle.secondary,
            label=label,
            emoji=_e(key) or None,
            custom_id=custom_id,
        )

    children: list = [ui.Separator(visible=True, spacing=SMALL)]
    if config.INFO_PANEL_BANNER_URL:
        children += [
            ui.MediaGallery(discord.MediaGalleryItem(config.INFO_PANEL_BANNER_URL)),
            ui.Separator(visible=True, spacing=SMALL),
        ]
    children += [
        ui.TextDisplay(f"## {_e('title')} 〃 __**G3 Service - Informations**__"),
        ui.Separator(visible=True, spacing=SMALL),
        ui.TextDisplay(
            f"> - {_e('note')} Before making a purchase, we recommend that you carefully read our "
            "__ToS__ and our __privacy policy__."
        ),
        ui.Separator(visible=True, spacing=SMALL),
    ]
    agree = ui.TextDisplay(
        f"> - {_e('note')} By reading the Terms of Service (ToS) and the Privacy Policy, "
        "you agree to these terms."
    )
    if config.INFO_PANEL_LOGO_URL:
        children.append(ui.Section(agree, accessory=ui.Thumbnail(config.INFO_PANEL_LOGO_URL)))
    else:
        children.append(agree)
    children += [
        ui.Separator(visible=True, spacing=SMALL),
        ui.ActionRow(
            btn(" 〃 ToS", "tos", "info:tos"),
            btn("〃 Privacy Policy", "privacy", "info:privacy"),
        ),
        ui.Separator(visible=True, spacing=SMALL),
        ui.TextDisplay(
            f"> -# {_e('footer')} 〃 **G3 Service, All Rights Reserved {_e('footer_right')} Informations**"
        ),
        ui.Separator(visible=True, spacing=SMALL),
    ]

    view = ui.LayoutView(timeout=None)
    view.add_item(ui.Container(*children, accent_colour=INFO_ACCENT))
    return view


LARGE = discord.SeparatorSpacing.large
DOT = _emoji('ui','bullet')


def _intro(text: ui.TextDisplay):
    """Intro block with the G3 Service logo as thumbnail (URL from config)."""
    if config.INFO_PANEL_LOGO_URL:
        return ui.Section(text, accessory=ui.Thumbnail(config.INFO_PANEL_LOGO_URL))
    return text


def _sep(spacing: discord.SeparatorSpacing = SMALL) -> ui.Separator:
    return ui.Separator(visible=True, spacing=spacing)


def _wrap(*children, accent: int) -> ui.LayoutView:
    view = ui.LayoutView(timeout=None)
    view.add_item(ui.Container(*children, accent_colour=accent))
    return view


def build_tos_view() -> ui.LayoutView:
    return _wrap(
        _sep(),
        ui.TextDisplay(f"## {_emoji('ui','tos')} 〃 __**Terms Of Service (ToS)**__"),
        _sep(),
        _intro(ui.TextDisplay(
            f"{_emoji('ui','arrow')} __By purchasing, accessing, or using any service provided by "
            "G3 Service, you agree to the following Terms of Service.__"
        )),
        _sep(LARGE),
        ui.TextDisplay(
            f" {DOT} ***__PURCHASES__***\n"
            "> -   All customers are responsible for reviewing a product before purchasing.\n"
            "> - By completing a purchase, you confirm that you understand what you are buying.\n"
            "> - You must provide accurate information when placing an order."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{DOT} ***__PAYMENTS__***\n"
            "> - Payment must be completed before a product is delivered unless otherwise agreed.\n"
            "> -  Do not send payment to unofficial members or unauthorized accounts.\n"
            "> -  lobal Bots is not responsible for payments sent to impersonators or unauthorized individuals."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{DOT} **__*PRODUCT USAGE*__**\n"
            "> -  Purchased products may only be used according to the license or permissions provided with the product.\n"
            "> - Redistributing, reselling, leaking, or sharing purchased products without permission is prohibited.\n"
            "> -  Attempting to remove protections or claim our products as your own is not permitted."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{DOT} ***__REFUNDS__***\n"
            "> - Refund eligibility depends on the product and the circumstances of the purchase.\n"
            "> - Once a product has been delivered, refunds may not be available.\n"
            "> - Contact Support before making a purchase if you have questions about a product."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{DOT} ***__SUPPORT__***\n"
            "> - Customers must communicate respectfully with our staff.\n"
            "> - False claims, harassment, threats, or abuse toward staff will not be tolerated.\n"
            "> - Please use the appropriate support ticket for your issue."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{DOT} **__*ACCOUNT & SERVER SECURITY*__**\n"
            "> - You are responsible for keeping your Discord account and purchased products secure.\n"
            "> - Never share passwords, tokens, API keys, or other sensitive credentials with anyone."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{DOT} **__*VIOLATIONS*__**\n"
            "> - G3 Service reserves the right to refuse service, cancel orders, or restrict access to our services when these Terms are violated."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{DOT} **__*CHANGES*__**\n"
            "> - G3 Service may update these Terms of Service when necessary. Continued use of our services after changes means you accept the updated Terms."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{_emoji('ui','close_alt')} 〃 ***__By purchasing from G3 Service, you acknowledge that you have "
            "read, understood, and agreed to these Terms of Service.__***"
        ),
        _sep(),
        ui.TextDisplay(f"> {_emoji('ui','arrow')} 〃 __Professional{DOT}Reliable{DOT}Secure__"),
        _sep(),
        ui.TextDisplay(f"{_emoji('ui','footer')} 〃 **G3 Service, All Rights Reserved** {DOT} **Terms of Service**"),
        _sep(),
        accent=0x007BFF,
    )


def build_privacy_view() -> ui.LayoutView:
    return _wrap(
        _sep(),
        ui.TextDisplay(f"## {_emoji('ui','privacy')} 〃 **__Privacy & Data Protection __**"),
        _sep(),
        _intro(ui.TextDisplay(
            f"> {_emoji('ui','arrow')} **Your privacy matters to us.**\n"
            " \n"
            f"> {_emoji('ui','arrow')}__ At G3 Service, we are committed to keeping your information safe and "
            "private. We only collect or use information that is necessary to provide our services, process "
            "orders, and provide customer support.__"
        )),
        _sep(LARGE),
        ui.TextDisplay(
            f"{_emoji('ui','privacy')} 〃 **What We Protect**\n\n"
            f"{DOT} Personal information\n"
            f"{DOT} Order and payment-related information\n"
            f"{DOT} Discord information required for support\n"
            f"{DOT} Messages and information shared through support tickets"
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{_emoji('ui','deny')} 〃 **What We Don’t Do**\n\n"
            f"{DOT} We do not sell your personal information.\n"
            f"{DOT} We do not share your information with unauthorized people.\n"
            f"{DOT} We do not use your information for purposes unrelated to our services."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f" {_emoji('ui','ticket')} 〃 **__*Support Tickets*__**\n\n\n"
            f"> {DOT} Please avoid sharing passwords, Discord tokens, payment-card numbers, or other highly sensitive information in tickets."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{_emoji('ui','purchase')} 〃 **__*Orders*__**\n\n\n"
            f"> {DOT} Information provided during an order is used only for fulfilling and managing that order and providing necessary support."
        ),
        _sep(LARGE),
        ui.TextDisplay(
            f"{_emoji('ui','privacy')} 〃 **__*Your Privacy = Our Responsibility*__**\n\n\n"
            f"> {DOT} ***By using our services, you agree to our Privacy Policy and understand that certain information may need to be processed to provide our services.***\n\n"
            f"{DOT} **If you have any questions regarding privacy or your data, please contact our Support Team.**\n"
        ),
        _sep(),
        ui.TextDisplay(f"{_emoji('ui','footer')} 〃 **G3 Service, All Rights Reserved {DOT} Privacy & Data Protection**"),
        _sep(),
        accent=0x006EFF,
    )


def build_faq_view() -> ui.LayoutView:
    def q(emoji_id: str, question: str, answer: str) -> list:
        return [
            ui.TextDisplay(f"{DOT} <:name:{emoji_id}> 〃 ***__{question}__***"),
            ui.TextDisplay(f"> {answer}"),
            _sep(LARGE),
        ]
    children += [
        ui.TextDisplay(f"**__Professional__{DOT} __Reliable__{DOT} __Secure__**"),
        ui.TextDisplay(f"{_emoji('ui','footer')} 〃** G3 Service, All Rights Reserved {DOT} Informations**"),
        _sep(),
    ]
    return _wrap(*children, accent=0x006EFF)


# key (the part after "info:") -> function returning the ephemeral view.
SECTION_BUILDERS: dict[str, Callable[[], ui.LayoutView]] = {
    "tos": build_tos_view,
    "privacy": build_privacy_view,
}


class InfoPanel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="panel-info", description="Send the Informations panel")
    @slash_is_ownership_only()
    async def panel_info(self, interaction: discord.Interaction):
        # Acknowledge first (Discord gives only 3 seconds), then post the panel.
        await interaction.response.defer(ephemeral=True, thinking=True)
        await interaction.channel.send(view=build_panel_view())
        await interaction.followup.send("Panel sent.", ephemeral=True)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type != discord.InteractionType.component:
            return
        custom_id = interaction.data.get("custom_id", "")
        if not custom_id.startswith("info:"):
            return

        builder = SECTION_BUILDERS.get(custom_id.split(":", 1)[1])
        if builder is None:
            await interaction.response.send_message("This section is not available yet.", ephemeral=True)
            return
        await interaction.response.send_message(view=builder(), ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(InfoPanel(bot))
