import os

# Fill in your real IDs below. Right-click a role/channel in Discord
# (Developer Mode on) and 'Copy ID'. Emoji live in emojis.py, not here.


def _env_or(env_name: str, value: str) -> str:
    """Render (or any host) env vars take priority over the value below,
    so secrets don't have to be committed to this file."""
    return os.environ.get(env_name, value)


GUILD_ID: int = 1464632674495758554
ROLE_DEVELOPER: int = 1569687193642082394
ROLE_CEO: int = 1569103584400777367
ROLE_CO_CEO: int = 1569104090682753135
ROLE_OWNERSHIP: int = 1569810300738342972
ROLE_STAFF: int = 1569104954377900094
ROLE_MANAGER: int = 1569810451066523778

# Convenience aliases used across cogs (bot_status, giveaways, permissions).
CEO_ROLE_ID: int = ROLE_CEO
OWNERSHIP_ROLE_ID: int = ROLE_OWNERSHIP

# --- LOG CHANNELS ---
# Purchase + Order tickets (opened / closed / transcript) are logged here.
CHANNEL_LOG: int = 1569817235164364870
CHANNEL_ORDERS: int = 1569811833282629795
CHANNEL_ORDERS_LOG: int = 1569811866363109447
LOG_GIVEAWAY_CHANNEL_ID: int = 1565870162605904022
REVIEWS_LOG_CHANNEL_ID: int = 1569812449287213076
SUGGESTIONS_CHANNEL_ID: int = 1569104247226638376

# Banner image shown at the top of every suggestion. Upload the image to Discord,
# copy its link and paste it here. Leave empty for no banner.
SUGGESTIONS_BANNER_URL: str = _env_or("SUGGESTIONS_BANNER_URL", "")

TICKET_CATEGORY: int = 1565870143584739338

# Each ticket "kind" now gets its own category. Fill in real IDs — 0 falls
# back to no category (channel created at the top level) until you do.
CATEGORY_PURCHASE: int = 1569811325847081001
CATEGORY_ORDER: int = 1569811105872744448
CATEGORY_OWNER: int = 1569811531904978994
CATEGORY_GENERAL: int = 1569811591220830359
CATEGORY_TECHNICAL: int = 1569811686918193162
CATEGORY_BILLING: int = 1569811764747440388
CATEGORY_MANAGER: int = 1569811794594242731

# Replacement tickets. Fill in the real category ID (0 = top level).
CATEGORY_REPLACEMENT: int = 1569813329159921787
TICKET_CATEGORIES: dict[str, int] = {
    "purchase": CATEGORY_PURCHASE,
    "order": CATEGORY_ORDER,
    "owner": CATEGORY_OWNER,
    "manager": CATEGORY_MANAGER,
    "general": CATEGORY_GENERAL,
    "technical": CATEGORY_TECHNICAL,
    "billing": CATEGORY_BILLING,
    "replacement": CATEGORY_REPLACEMENT,
}

# --- Unified Ticket Center panel (/send-ticket-center). Replace the URLs with
# your own images. None = skip that element. ---
TICKET_CENTER_BANNER_URL: str | None = "https://i.imgur.com/j4myBBI.jpeg"
TICKET_CENTER_THUMBNAIL_URL: str | None = "https://i.imgur.com/ppkRp7r.jpeg"
TICKET_CENTER_FOOTER_GIF_URL: str | None = ""

# Target of the "Informations" link button on the panel.
TICKET_CENTER_INFO_URL: str = "https://discord.com/channels/1464632674495758554/1569817443835183194"

TRANSCRIPT_BANNER_URL: str | None = "https://i.imgur.com/j4myBBI.jpeg"
TRANSCRIPT_LOGO_URL: str | None = "https://i.imgur.com/ppkRp7r.jpeg"

# Logo used by the Informations panel.
PURCHASE_PANEL_LOGO_URL: str | None = "https://i.imgur.com/ppkRp7r.jpeg"

# --- Informations panel (/panel-info). Set a URL, or None to skip that element. ---
# Banner: replace with the URL of your global_banner image (currently reuses the purchase banner).
INFO_PANEL_BANNER_URL: str | None = "https://i.imgur.com/j4myBBI.jpeg"
INFO_PANEL_LOGO_URL: str | None = PURCHASE_PANEL_LOGO_URL  # GLOBAL_LOGO

# --- Ticket staff roles per ticket kind ---
# staff_roles is its own list of role IDs — fill it in yourself, it can
# overlap with or differ from ROLE_DEVELOPER/ROLE_CEO/ROLE_CO_CEO above.
# (Each support kind now has its own category above in TICKET_CATEGORIES —
# CATEGORY_OWNER / CATEGORY_GENERAL / CATEGORY_TECHNICAL / CATEGORY_BILLING /
# CATEGORY_REPLACEMENT.)
TICKET_KIND_STAFF_ROLES: dict[str, list[int]] = {
    "owner": [ROLE_OWNERSHIP],
    "order": [ROLE_OWNERSHIP, ROLE_DEVELOPER],
    "purchase": [ROLE_OWNERSHIP],
    "general": [ROLE_STAFF, ROLE_MANAGER],
    "technical": [ROLE_DEVELOPER, ROLE_OWNERSHIP],
    "manager": [ROLE_MANAGER],
    "billing": [ROLE_OWNERSHIP],
    "replacement": [ROLE_DEVELOPER, ROLE_OWNERSHIP],
}

# All the other tickets (owner, manager, general, technical, billing, replacement) are logged here.
SUPPORT_LOG_CHANNEL: int = 1569813329159921787

# --- Giveaways / Reviews banners ---
GIVEAWAY_BANNER_URL: str | None = "https://i.imgur.com/j4myBBI.jpeg"
REVIEWS_BANNER_URL: str | None = "https://i.imgur.com/j4myBBI.jpeg"
REVIEWS_LOG_BANNER__URL: str | None = "https://i.imgur.com/j4myBBI.jpeg"
TICKET_PANEL_BANNER_URL: str | None = "https://i.imgur.com/j4myBBI.jpeg"

# --- Shared application settings (used by Manager / Staff as fallback) ---
# Category where each applicant's private application channel is created
# (0 = no category, channel is created at the top level).
APPLICATIONS_CATEGORY_ID: int = 1569813803703734322

# Staff-only channel where submitted applications arrive for review. REQUIRED —
# applicants can't press "Sent" until this is filled in.
APPLICATIONS_LOG_CHANNEL_ID: int = 1569813885274300466

# Roles that can see the application channels, use Ping User / Close.
APPLICATION_STAFF_ROLE_IDS: list[int] = [ROLE_OWNERSHIP, ROLE_CEO, ROLE_CO_CEO]

# Roles that can Accept / Deny and use Show Answers in the log channel.
APPLICATION_REVIEW_ROLE_IDS: list[int] = [ROLE_OWNERSHIP, ROLE_CEO, ROLE_CO_CEO]

# Role given to the applicant when accepted (0 = give no role).
APPLICATION_ACCEPTED_ROLE_ID: int = 1569104954377900094

# Banner shown at the top of the application panel (empty = no banner).
APPLICATIONS_BANNER_URL: str | None = "https://i.imgur.com/j4myBBI.jpeg"

# --- Staff / Manager applications (/panel-staff-applications) ---
# TEXT ONLY: no photos, files or
# image links are accepted or shown. Every setting below is optional: 0 / None
# falls back to the shared application setting above.
STAFF_APPLICATIONS_BANNER_URL: str | None = APPLICATIONS_BANNER_URL
STAFF_APPLICATIONS_LOGO_URL: str | None = PURCHASE_PANEL_LOGO_URL

# One shared Manager + Staff panel, but each type has its OWN application category and log channel.
# Fill in the real IDs (0 = fall back to the shared application setting).
MANAGER_APPLICATIONS_CATEGORY_ID: int = 1569813803703734322
MANAGER_APPLICATIONS_LOG_CHANNEL_ID: int = 1569814181484433539
STAFF_APPLICATIONS_CATEGORY_ID: int = 1569813803703734322
STAFF_APPLICATIONS_LOG_CHANNEL_ID: int = 1569813885274300466

# Roles given to the applicant when accepted (0 = give no role).
MANAGER_APPLICATION_ACCEPTED_ROLE_ID: int = ROLE_MANAGER
STAFF_APPLICATION_ACCEPTED_ROLE_ID: int = ROLE_STAFF

# Questions (Greek + English). Plain string = typed answer; use {"text": ..., "type": "yesno"}
# for Yes / No buttons.
MANAGER_QUESTIONS: list = [
    "Διαθέτετε προηγούμενη εμπειρία σε διοικητική θέση;\n/ Do you have any previous experience in a management position?",
    "Ποια θεωρείτε τα βασικότερα χαρακτηριστικά ενός επιτυχημένου Manager;\n/ What do you consider the key qualities of a successful Manager?",
    "Πώς θα διαχειριζόσασταν μια σύγκρουση μεταξύ δύο Staff Members;\n/ How would you handle a conflict between two Staff Members?",
    "Πώς θα αντιμετωπίζατε ένα μέλος της ομάδας με επανειλημμένα χαμηλή απόδοση;\n/ How would you deal with a team member who consistently underperforms?",
    "Πώς θα διασφαλίζατε την ομαλή λειτουργία του καταστήματος;\n/ How would you ensure the smooth operation of the shop?",
    "Πώς θα ενεργούσατε σε περίπτωση σοβαρού προβλήματος χωρίς τη διαθεσιμότητα του Owner;\n/ How would you handle a serious issue if the Owner was unavailable?",
    "Ποια θα ήταν η πρώτη σας προτεραιότητα κατά την ανάληψη της θέσης Manager;\n/ What would be your first priority upon taking on the Manager position?",
]

STAFF_QUESTIONS: list = [
    "Ποια είναι η ηλικία σας και πόσο χρόνο μπορείτε να διαθέσετε καθημερινά;\n/ What is your age, and how much time can you dedicate daily?",
    "Διαθέτετε προηγούμενη εμπειρία σε αντίστοιχη θέση;\n/ Do you have any previous experience in a similar position?",
    "Για ποιον λόγο επιθυμείτε να ενταχθείτε στο προσωπικό μας;\n/ Why would you like to join our staff team?",
    "Πώς θα διαχειριζόσασταν έναν δυσαρεστημένο πελάτη;\n/ How would you handle a dissatisfied customer?",
    "Πώς θα ενεργούσατε εάν δεν γνωρίζατε την απάντηση σε ερώτημα πελάτη;\n/ How would you respond if you did not know the answer to a customer's question?",
    "Πώς θα διαχειριζόσασταν μια παραβίαση κανονισμών από συνάδελφό σας;\n/ How would you handle a rule violation committed by another staff member?",
    "Ποιο θεωρείτε το σημαντικότερο χαρακτηριστικό ενός επαγγελματία Staff Member;\n/ What do you consider the most important quality of a professional Staff Member?",
]

# Application types. The custom_id on each panel button is "app_apply:<key>".
# "photos": False turns the photo system off for that type.
APPLICATION_TYPES: dict[str, dict] = {
    "manager": {
        "label": "Manager",
        "questions": MANAGER_QUESTIONS,
        "photos": False,
        "accepted_role_id": MANAGER_APPLICATION_ACCEPTED_ROLE_ID,
        "category_id": MANAGER_APPLICATIONS_CATEGORY_ID,
        "log_channel_id": MANAGER_APPLICATIONS_LOG_CHANNEL_ID,
    },
    "staff": {
        "label": "Staff",
        "questions": STAFF_QUESTIONS,
        "photos": False,
        "accepted_role_id": STAFF_APPLICATION_ACCEPTED_ROLE_ID,
        "category_id": STAFF_APPLICATIONS_CATEGORY_ID,
        "log_channel_id": STAFF_APPLICATIONS_LOG_CHANNEL_ID,
    },
}

# --- Invites panel (/panel-invites). Banner image URL, or None to skip. ---
INVITES_BANNER_URL: str | None = "https://i.imgur.com/j4myBBI.jpeg"

# Channel where join/leave invite logs are sent (its own channel, separate from the ticket logs).
INVITES_LOG_CHANNEL_ID: int = 1565870155840618797
BOT_TOKEN: str = _env_or("BOT_TOKEN", "PUT_YOUR_BOT_TOKEN_HERE")

TURSO_URL: str = _env_or("TURSO_URL", "libsql://your-database-name.turso.io")
TURSO_AUTH_TOKEN: str = _env_or("TURSO_AUTH_TOKEN", "PUT_YOUR_TURSO_AUTH_TOKEN_HERE")

# Render (and other hosts) require the process to bind to a port so their
# health check passes. This does not need to be a "real" web server.
KEEP_ALIVE_PORT: int = int(os.environ.get("PORT", 1000))


def staff_role_ids() -> list[int]:
    """Roles allowed to view/manage every ticket (Developer, CEO, Co-CEO)."""
    return [ROLE_DEVELOPER, ROLE_CEO, ROLE_CO_CEO]
