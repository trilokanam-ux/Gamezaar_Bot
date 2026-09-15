import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonCommands,
    WebAppInfo,
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# =========================
# LOAD ENV
# =========================

BOT_TOKEN   = os.environ.get("BOT_TOKEN")
WEBAPP_URL  = os.environ.get("WEBAPP_URL")
SUPPORT_URL = os.environ.get("SUPPORT_URL")


# =========================
# OPEN (PLAY) BUTTON
# =========================

def play_button():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(text="▶️ Play", web_app=WebAppInfo(url=WEBAPP_URL))
    ]])


# =========================
# SUPPORT BUTTON
# =========================

def support_button():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(text="Support", url=SUPPORT_URL)
    ]])


# =========================
# START COMMAND
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Welcome to Gamezaar!\n\n"
        "Your personal gaming hub for quick, casual play — right inside Telegram. "
        "Explore game categories, learn more about us, or get support. New here? Just tap /board to begin."
    )
    await update.message.reply_text(text=text, reply_markup=play_button())


# =========================
# CATEGORY COMMANDS
# =========================

async def board(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 Board Games\n\n"
        "Classic board games, reimagined for quick play. Jump into a match with friends "
        "anytime — no downloads, no hassle.",
        reply_markup=play_button()
    )

async def card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🃏 Card Games\n\n"
        "Skill-based card games for a fast, casual match whenever you've got a few minutes to spare.",
        reply_markup=play_button()
    )

async def puzzle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧩 Puzzle Games\n\n"
        "Quick brain teasers and number puzzles for a relaxing break, anytime you need one.",
        reply_markup=play_button()
    )

async def strategy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "♟️ Strategy\n\n"
        "Plan your moves and outsmart your opponents. Casual strategy play, made for quick sessions.",
        reply_markup=play_button()
    )

async def racing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏎️ Racing\n\n"
        "Fast, casual racing action — jump in, race, and see how you stack up. No downloads needed.",
        reply_markup=play_button()
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ About Gamezaar\n\n"
        "Your personal gaming hub for quick, casual play — anytime, anywhere, right inside Telegram."
    )

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Support\n\n"
        "Have an issue or question? Our team typically responds within 24 hours on business days.",
        reply_markup=support_button()
    )


# =========================
# SETUP MENU COMMANDS
# =========================

async def setup_commands(app):
    commands = [
        ("start",    "Welcome & main menu"),
        ("board",    "Board Games"),
        ("card",     "Card Games"),
        ("puzzle",   "Puzzle Games"),
        ("strategy", "Strategy Games"),
        ("racing",   "Racing Games"),
        ("about",    "About Gamezaar"),
        ("support",  "Get help"),
    ]
    await app.bot.set_my_commands(commands)
    await app.bot.set_chat_menu_button(menu_button=MenuButtonCommands())


async def post_init(app):
    await setup_commands(app)


# =========================
# CREATE APP
# =========================

app = (
    Application.builder()
    .token(BOT_TOKEN)
    .post_init(post_init)
    .build()
)

app.add_handler(CommandHandler("start",    start))
app.add_handler(CommandHandler("board",    board))
app.add_handler(CommandHandler("card",     card))
app.add_handler(CommandHandler("puzzle",   puzzle))
app.add_handler(CommandHandler("strategy", strategy))
app.add_handler(CommandHandler("racing",   racing))
app.add_handler(CommandHandler("about",    about))
app.add_handler(CommandHandler("support",  support))


# =========================
# START BOT
# =========================

print("✅ Gamezaar Bot Running...")
app.run_polling()
