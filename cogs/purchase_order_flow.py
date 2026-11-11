from __future__ import annotations

import discord
from emojis import emoji as _emoji


PAYMENT_METHODS = ("PayPal", "PaySafe", "LTC")


# --------------------------------------------------------------------------
# Purchase flow: modal (Product / Budget / Server / Description) -> PayPal/Paysafe/LTC -> Send/Cancel
# --------------------------------------------------------------------------

class PurchaseModal(discord.ui.Modal, title="Purchase a Product"):
    product = discord.ui.TextInput(
        label="Which product are you interested in?",
        placeholder="e.g. Moderation bot, Roleplay bot, Security bot...",
        max_length=200,
    )
    budget = discord.ui.TextInput(
        label="What's your budget?",
        placeholder="e.g. 20€",
        max_length=100,
    )
    server = discord.ui.TextInput(
        label="Server link & name",
        placeholder="Paste the server invite link and the server name",
        max_length=200,
    )
    description = discord.ui.TextInput(
        label="Description",
        style=discord.TextStyle.paragraph,
        placeholder="Anything specific you'd like us to know...",
        max_length=1000,
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            view=PurchasePaymentView(
                self.product.value, self.budget.value, self.server.value, self.description.value
            ),
            ephemeral=True,
        )


class PurchasePaymentView(discord.ui.LayoutView):
    """Second step of the purchase flow: pick PayPal / Paysafe / LTC, then Send."""

    def __init__(
        self, product: str, budget: str, server: str, description: str, payment: str | None = None
    ) -> None:
        super().__init__(timeout=300)
        self.product = product
        self.budget = budget
        self.server = server
        self.description = description
        self.payment = payment
        self._build()

    def _build(self) -> None:
        payment_buttons = []
        for method in PAYMENT_METHODS:
            btn = discord.ui.Button(
                label=method,
                style=discord.ButtonStyle.success if self.payment == method else discord.ButtonStyle.secondary,
                disabled=(self.payment is not None and self.payment != method),
            )
            btn.callback = self._payment_callback(method)
            payment_buttons.append(btn)

        send_btn = discord.ui.Button(
            label="Send", style=discord.ButtonStyle.success,
            emoji=(_emoji('general', 'send') or None), disabled=not self.payment,
        )
        send_btn.callback = self.on_send

        cancel_btn = discord.ui.Button(
            label="Cancel", style=discord.ButtonStyle.danger, emoji=(_emoji('general', 'cancel') or None)
        )
        cancel_btn.callback = self.on_cancel

        summary = (
            f"**Product:** {self.product}\n"
            f"**Budget:** {self.budget}\n"
            f"**Server:** {self.server}\n"
            f"**Payment:** {self.payment or '*not set*'}"
        )

        container = discord.ui.Container(
            discord.ui.TextDisplay(f"{_emoji('general', 'purchase')} **Purchase a Product**"),
            discord.ui.TextDisplay(summary),
            discord.ui.TextDisplay(f"**Description:**\n{self.description}"),
            discord.ui.Separator(),
            discord.ui.ActionRow(*payment_buttons),
            discord.ui.ActionRow(send_btn, cancel_btn),
            accent_colour=discord.Colour.green(),
        )
        self.add_item(container)

    def _payment_callback(self, payment: str):
        async def callback(interaction: discord.Interaction) -> None:
            new_payment = None if self.payment == payment else payment
            await interaction.response.edit_message(
                view=PurchasePaymentView(
                    self.product, self.budget, self.server, self.description, new_payment
                )
            )
        return callback

    async def on_send(self, interaction: discord.Interaction) -> None:
        from cogs.tickets import create_ticket_channel

        fields = {
            "product": self.product,
            "budget": self.budget,
            "server": self.server,
            "description": self.description,
            "payment_method": self.payment,
        }
        await create_ticket_channel(interaction, kind="purchase", fields=fields)

    async def on_cancel(self, interaction: discord.Interaction) -> None:
        cancelled_view = discord.ui.LayoutView(timeout=None)
        cancelled_view.add_item(
            discord.ui.Container(
                discord.ui.TextDisplay(f"{_emoji('general', 'cancel')} Cancelled."),
                accent_colour=discord.Colour.red(),
            )
        )
        await interaction.response.edit_message(view=cancelled_view)


# --------------------------------------------------------------------------
# Order flow: modal (server/description/budget) -> PayPal/Paysafe/LTC -> Send/Cancel
# --------------------------------------------------------------------------

class OrderInfoModal(discord.ui.Modal, title="Order a Custom Bot"):
    server = discord.ui.TextInput(
        label="Server link & name",
        placeholder="Paste the server invite link and the server name",
        max_length=200,
    )
    description = discord.ui.TextInput(
        label="Describe what you want",
        style=discord.TextStyle.paragraph,
        placeholder="Features, style, anything specific you'd like...",
        max_length=1000,
    )
    budget = discord.ui.TextInput(
        label="What's your budget?",
        placeholder="e.g. 20€",
        max_length=100,
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            view=OrderPaymentView(self.server.value, self.description.value, self.budget.value),
            ephemeral=True,
        )


class OrderPaymentView(discord.ui.LayoutView):
    def __init__(
        self, server: str, description: str, budget: str, payment: str | None = None
    ) -> None:
        super().__init__(timeout=300)
        self.server = server
        self.description = description
        self.budget = budget
        self.payment = payment
        self._build()

    def _build(self) -> None:
        payment_buttons = []
        for method in PAYMENT_METHODS:
            btn = discord.ui.Button(
                label=method,
                style=discord.ButtonStyle.success if self.payment == method else discord.ButtonStyle.secondary,
                disabled=(self.payment is not None and self.payment != method),
            )
            btn.callback = self._payment_callback(method)
            payment_buttons.append(btn)

        ready = bool(self.payment)
        send_btn = discord.ui.Button(
            label="Send", style=discord.ButtonStyle.success, emoji=(_emoji('general','send') or None), disabled=not ready
        )
        send_btn.callback = self.on_send

        cancel_btn = discord.ui.Button(label="Cancel", style=discord.ButtonStyle.danger, emoji=(_emoji('general','cancel') or None))
        cancel_btn.callback = self.on_cancel

        summary = (
            f"**Server:** {self.server}\n"
            f"**Budget:** {self.budget}\n"
            f"**Payment:** {self.payment or '*not set*'}"
        )

        container = discord.ui.Container(
            discord.ui.TextDisplay(f"{_emoji('general','order')} **Order a Custom Bot**"),
            discord.ui.TextDisplay(summary),
            discord.ui.TextDisplay(f"**Description:**\n{self.description}"),
            discord.ui.Separator(),
            discord.ui.ActionRow(*payment_buttons),
            discord.ui.ActionRow(send_btn, cancel_btn),
            accent_colour=discord.Colour.blue(),
        )
        self.add_item(container)

    def _payment_callback(self, payment: str):
        async def callback(interaction: discord.Interaction) -> None:
            new_payment = None if self.payment == payment else payment
            await interaction.response.edit_message(
                view=OrderPaymentView(self.server, self.description, self.budget, new_payment)
            )
        return callback

    async def on_send(self, interaction: discord.Interaction) -> None:
        from cogs.tickets import create_ticket_channel

        fields = {
            "server": self.server,
            "description": self.description,
            "budget": self.budget,
            "payment_method": self.payment,
        }
        await create_ticket_channel(interaction, kind="order", fields=fields)

    async def on_cancel(self, interaction: discord.Interaction) -> None:
        cancelled_view = discord.ui.LayoutView(timeout=None)
        cancelled_view.add_item(
            discord.ui.Container(discord.ui.TextDisplay(f"{_emoji('general','cancel')} Cancelled."), accent_colour=discord.Colour.red())
        )
        await interaction.response.edit_message(view=cancelled_view)


# --------------------------------------------------------------------------
# Entrypoints — called from the main ticket panel's Purchase / Order buttons
# --------------------------------------------------------------------------

async def start_purchase_flow(interaction: discord.Interaction) -> None:
    await interaction.response.send_modal(PurchaseModal())


async def start_order_flow(interaction: discord.Interaction) -> None:
    await interaction.response.send_modal(OrderInfoModal())
