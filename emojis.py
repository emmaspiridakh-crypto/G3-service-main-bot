GENERAL = {
    "purchase": "<:purchase:0>",
    "order": "<:order:0>",
    "close": "<:close:0>",
    "claim": "<:claim:0>",
    "ping": "<:ping:0>",
    "transcript": "<:transcript:0>",
    "bot": "<:bot:0>",
    "budget": "<:budget:0>",
    "payment": "<:payment:0>",
    "log_open": "<a:log_open:0>",
    "place_order": "<a:place_order:0>",
    "order_accept": "<:order_accept:0>",
    "order_done": "<:order_done:0>",
    "order_cancel": "<:order_cancel:0>",
    "order_pending": "<a:order_pending:0>",
    "check": "<:check:0>",
    "cancel": "<:cancel:0>",
    "send": "<a:send:0>",
    "plan": "<:plan:0>",
    "server": "<:server:0>",
    "modify": "<:modify:0>",
}

SUGGESTIONS = {
    "upvote": "<:upvote:0>",
    "downvote": "<:downvote:0>",
    "remove": "<:remove:0>",
    "total": "<:total:0>",
    "time": "<:time:0>",
    "footer_left": "<:footer_left:0>",
    "suggestion": "<:suggestion:0>",
    "submitted": "<:submitted:0>",
    "bullet": "<:bullet:0>",
}

REVIEWS = {
    "review": "<:review:0>",
    "star_filled": "<:star_filled:0>",
    "star_empty": "<:star_empty:0>",
}

GIVEAWAY = {
    "giveaway": "<:giveaway:0>",
    "join": "<:join:0>",
    "leave": "<:leave:0>",
    "info": "<:info:0>",
    "edit": "<:edit:0>",
    "reroll": "<:reroll:0>",
    "end": "<:end:0>",
    "participants": "<:participants:0>",
    "winner": "<:winner:0>",
    "prize": "<:prize:0>",
    "host": "<:host:0>",
    "winners_count": "<:winners_count:0>",
    "entries": "<:entries:0>",
    "time": "<:time:0>",
    "role": "<:role:0>",
    "add_member": "<:add_member:0>",
}

APPLICATIONS = {
    "yes": "<:yes:0>",
    "no": "<:no:0>",
    "send": "<a:send:0>",
    "accept": "<:accept:0>",
    "deny": "<:deny:0>",
    "close": "<:close:0>",
    "ping": "<:ping:0>",
}

INFO = {
    "title": "<:title:0>",
    "note": "<a:note:0>",
    "tos": "<:tos:0>",
    "privacy": "<:privacy:0>",
    "faq": "<:faq:0>",
    "footer": "<:footer:0>",
    "footer_right": "<:footer_right:0>",
}

INVITES = {
    "title": "<a:title:0>",
    "panel_info": "<:panel_info:0>",
    "my_invites": "<:my_invites:0>",
    "leaderboard": "<:leaderboard:0>",
    "joins": "<:joins:0>",
    "left": "<:left:0>",
    "remaining": "<:remaining:0>",
    "rank": "<:rank:0>",
    "first": "<:first:0>",
    "second": "<:second:0>",
    "third": "<:third:0>",
    "bullet": "<:bullet:0>",
    "footer": "<:footer:0>",
    "log_join": "<:log_join:0>",
    "log_leave": "<:log_leave:0>",
    "user": "<:user:0>",
    "inviter": "<:inviter:0>",
}

# Shared emoji used in panels, tickets, reviews, info, applications...
UI = {
    "bullet": "<:bullet:0>",
    "footer": "<:footer:0>",
    "arrow": "<:arrow:0>",
    "server": "<:server:0>",
    "yes": "<:yes:0>",
    "no": "<:no:0>",
    "note": "<a:note:0>",
    "star": "<:star:0>",
    "close": "<:close:0>",
    "ping": "<:ping:0>",
    "claim": "<:claim:0>",
    "modify": "<:modify:0>",
    "transcript": "<:transcript:0>",
    "payment": "<:payment:0>",
    "order": "<:order:0>",
    "purchase": "<:purchase:0>",
    "replace": "<:replace:0>",
    "owner": "<:owner:0>",
    "manager": "<:manager:0>",
    "staff": "<:staff:0>",
    "user": "<:user:0>",
    "ticket": "<:ticket:0>",
    "welcome": "<:welcome:0>",
    "process": "<:process:0>",
    "deny": "<:deny:0>",
    "close_alt": "<:close_alt:0>",
    "info": "<:info:0>",
    "tos": "<:tos:0>",
    "privacy": "<:privacy:0>",
    "applications": "<:applications:0>",
    "ticket_center": "<:ticket_center:0>",
    "support": "<:support:0>",
}

_CATEGORIES = {
    "invites": INVITES,
    "info": INFO,
    "applications": APPLICATIONS,
    "general": GENERAL,
    "suggestions": SUGGESTIONS,
    "reviews": REVIEWS,
    "giveaway": GIVEAWAY,
    "ui": UI,
}

EMOJI: dict = GENERAL


def emoji(category: str, key: str) -> str:
    """Return the emoji markup, or "" while its ID is still 0 (not filled in yet)
    so the bot shows no broken ':name:' text and buttons don't error."""
    value = _CATEGORIES.get(category, {}).get(key, "")
    if not value or value.rstrip(">").endswith(":0"):
        return ""
    return value
