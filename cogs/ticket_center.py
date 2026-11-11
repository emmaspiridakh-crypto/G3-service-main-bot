"""
Unified Ticket Center panel — Support, Purchase and Issues/Replacement in ONE
panel (/send-ticket-center). Existing systems are untouched: every option
reuses the same flows as before (support modal / purchase flow / order flow
-> create_ticket_channel). The old panels keep working.

All image/link URLs come from config.py (TICKET_CENTER_*).
"""
from __future__ import annotations

import discord
from emojis import emoji as _emoji
from discord import app_commands, ui
from discord.ext import commands

import config
from cogs.support_tickets import ProblemModal

SMALL = discord.SeparatorSpacing.small


async def _reset_panel(interaction: discord.Interaction) -> None:
    """Re-posts the panel's own view so the select menus go back to their
    placeholder — otherwise Discord keeps showing the last choice and picking
    the same option twice would not fire again."""
    try:
        if interaction.message is not None:
            await interaction.message.edit(view=TicketCenterView())
    except discord.HTTPException:
        pass


class TicketCenterView(ui.LayoutView):
    def __init__(self) -> None:
        super().__init__(timeout=None)

        sep = lambda visible=True: ui.Separator(visible=visible, spacing=SMALL)  # noqa: E731

        # -- selects (custom_ids are unique to this panel)
        support_select = ui.Select(
            custom_id="ticketcenter:support",
            placeholder="@📞 〃 Support Center ",
            options=[
                discord.SelectOption(label="〃 Owner ", value="owner",
                                     description="Talk with the administrator ", emoji=(_emoji('ui','owner') or None)),
                discord.SelectOption(label="〃 Management ", value="manager",
                                     description="Talk with the management team", emoji=(_emoji('ui','manager') or None)),
                discord.SelectOption(label="〃 General Support ", value="general",
                                     description="Talk with the staff team", emoji=(_emoji('ui','staff') or None)),
            ],
        )
        support_select.callback = self.on_support

        purchase_select = ui.Select(
            custom_id="ticketcenter:purchase",
            placeholder="@💰 〃 Purchase Center ",
            options=[
                discord.SelectOption(label="〃 Order ", value="order",
                                     description="Order a custom product ", emoji=(_emoji('ui','order') or None)),
                discord.SelectOption(label="〃 Purchase ", value="purchase",
                                     description="Purchase an existing product", emoji=(_emoji('ui','payment') or None)),
            ],
        )
        purchase_select.callback = self.on_purchase

        issues_select = ui.Select(
            custom_id="ticketcenter:issues",
            placeholder="@⚙️ 〃 Issues/Replacement ",
            options=[
                discord.SelectOption(label="〃 Technical Issue ", value="technical",
                                     description="Problem with the product", emoji=(_emoji('ui','modify') or None)),
                discord.SelectOption(label="〃 Payment Issue ", value="billing",
                                     description="Problem with the payment ", emoji=(_emoji('ui','payment') or None)),
                discord.SelectOption(label="〃 Replacement ", value="replacement",
                                     description="Replace a product ", emoji=(_emoji('ui','replace') or None)),
            ],
        )
        issues_select.callback = self.on_issues

        children: list = [sep()]
        if config.TICKET_CENTER_BANNER_URL:
            children += [ui.MediaGallery(discord.MediaGalleryItem(config.TICKET_CENTER_BANNER_URL)), sep()]

        children += [
            ui.TextDisplay(f"# {_emoji('ui','ticket_center')} 〃 __***G3 Service™ - Ticket Center***__"),
            sep(),
        ]
        welcome = ui.TextDisplay(
            "***__Welcome to our Ticket Center.__***\n"
            "\n"
            f"> {_emoji('ui','note')} Before you do anything we suggest to learn about our Terms of Service and our Privacy."
        )
        if config.TICKET_CENTER_THUMBNAIL_URL:
            children.append(ui.Section(welcome, accessory=ui.Thumbnail(config.TICKET_CENTER_THUMBNAIL_URL)))
        else:
            children.append(welcome)
        children.append(sep())
        if config.TICKET_CENTER_INFO_URL:
            children += [
                ui.ActionRow(
                    ui.Button(
                        style=discord.ButtonStyle.link,
                        label="〃 Informations",
                        emoji=(_emoji('ui','info') or None),
                        url=config.TICKET_CENTER_INFO_URL,
                    ),
                ),
                sep(),
            ]
        children += [
            ui.TextDisplay(f"## {_emoji('ui','support')} 〃 __***Support Center***__ "),
            ui.TextDisplay(
                "*If you need any help or have any questions, choose the appropriate category*. \n"
                f"> {_emoji('ui','bullet')} **Owner** — Talk directly with the administrator \n"
                f"> {_emoji('ui','bullet')} **Management** — Talk with the management team\n"
                f"> {_emoji('ui','bullet')} **General Support** — Talk with the staff team\n"
            ),
            sep(),
            ui.ActionRow(support_select),
            sep(),
            ui.TextDisplay(f"## {_emoji('ui','purchase')} 〃 __***Purchase Center***__"),
            ui.TextDisplay(
                "*To purchase a custom product or to order an existing product.*\n"
                f"> {_emoji('ui','bullet')} **Order** — To order a custom product suited to your needs\n"
                f"> {_emoji('ui','bullet')} **Purchase** — To buy an existing product"
            ),
            sep(),
            ui.ActionRow(purchase_select),
            sep(),
            ui.TextDisplay(f"## {_emoji('ui','modify')} 〃 ***__Issues/Replacement__*** "),
            ui.TextDisplay(
                "*If you want a product replacement, something goes wrong with the product or the payment. * \n"
                f"> {_emoji('ui','bullet')} **Technical Issue** — Problem with the product\n"
                f"> {_emoji('ui','bullet')} **Payment Issue** — Problem with the payment or questions \n"
                f"> {_emoji('ui','bullet')} **Replacement** — Replace a product "
            ),
            sep(),
            ui.ActionRow(issues_select),
            sep(),
            ui.TextDisplay(f"### {_emoji('ui','process')} 〃 __**TICKET PROCESS**__   "),
            ui.TextDisplay(
                f"> {_emoji('ui','note')} Choose the category that best matches your request.\n"
                f"> {_emoji('ui','note')} Please provide a proper description of your issue or request.\n"
                f"> {_emoji('ui','note')} Our Team will review your ticket and assist you as soon as possible.\n"
                f"> {_emoji('ui','note')} Please don't open an owner ticket without an important reason. This action may result in a warning "
            ),
            sep(),
        ]
        if config.TICKET_CENTER_FOOTER_GIF_URL:
            children += [ui.MediaGallery(discord.MediaGalleryItem(config.TICKET_CENTER_FOOTER_GIF_URL)), sep()]
        children += [
            ui.TextDisplay(
                f" {_emoji('ui','footer')} 〃 **G3 Service™, All Rights Reserved ©** "
                f"{_emoji('ui','bullet')} **Ticket  Center** "
            ),
            sep(),
        ]
        self.add_item(ui.Container(*children, accent_colour=0x0062FF))

    # -- callbacks: same flows the old panels used --------------------------
    async def on_support(self, interaction: discord.Interaction) -> None:
        kind = interaction.data["values"][0]
        await interaction.response.send_modal(ProblemModal(kind))
        await _reset_panel(interaction)

    async def on_issues(self, interaction: discord.Interaction) -> None:
        kind = interaction.data["values"][0]
        await interaction.response.send_modal(ProblemModal(kind))
        await _reset_panel(interaction)

    async def on_purchase(self, interaction: discord.Interaction) -> None:
        from cogs.purchase_order_flow import start_order_flow, start_purchase_flow

        choice = interaction.data["values"][0]
        if choice == "order":
            await start_order_flow(interaction)
        else:
            await start_purchase_flow(interaction)
        await _reset_panel(interaction)


class TicketCenter(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="send-ticket-center",
        description="Ticket Center panel",
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def send_ticket_center(self, interaction: discord.Interaction) -> None:
        await interaction.channel.send(view=TicketCenterView())
        await interaction.response.send_message("panel sent.", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    bot.add_view(TicketCenterView())
    await bot.add_cog(TicketCenter(bot))
