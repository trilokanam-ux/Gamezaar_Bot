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
        "👋 Welcome to Gametion Bot!\n\n"
        "Use the menu below or type a command to explore game categories, learn about us, "
        "or get support. New here? Just tap /board to begin."
    )
    await update.message.reply_text(text=text, reply_markup=play_button())


# =========================
# CATEGORY COMMANDS
# =========================

async def board(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 Board Games\n\n"
        "Classic board games reimagined for mobile — familiar rules, smooth multiplayer, "
        "and quick matches with friends. Perfect for family game nights and friendly rivalries.",
        reply_markup=play_button()
    )

async def card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🃏 Card Games\n\n"
        "Skill-based card games with real-time matches and competitive play. "
        "Sharpen your strategy and outsmart opponents online.",
        reply_markup=play_button()
    )

async def puzzle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧩 Puzzle Games\n\n"
        "Daily brain training with number logic and clean, focused puzzle play. "
        "Great for relaxing your mind anytime, anywhere.",
        reply_markup=play_button()
    )

async def strategy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "♟️ Strategy\n\n"
        "Think ahead, plan your moves, and outwit your opponents. "
        "Strategy games for players who love a good mental challenge.",
        reply_markup=play_button()
    )

async def racing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏎️ Racing\n\n"
        "High-speed racing action with smooth controls and competitive leaderboards. "
        "Race friends or players worldwide for the top spot.",
        reply_markup=play_button()
    )

async def trivia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 Trivia\n\n"
        "Test your knowledge across countless topics in fast, fun trivia matches. "
        "Challenge friends and climb the leaderboard.",
        reply_markup=play_button()
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ About Gametion\n\n"
        "Gametion Technologies builds mobile-first games designed for daily play and social fun — "
        "trusted by millions worldwide. Committed to quality entertainment since day one."
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
        ("trivia",   "Trivia Games"),
        ("about",    "About Gametion"),
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
app.add_handler(CommandHandler("trivia",   trivia))
app.add_handler(CommandHandler("about",    about))
app.add_handler(CommandHandler("support",  support))


# =========================
# START BOT
# =========================

print("✅ Gametion Bot Running...")
app.run_polling()