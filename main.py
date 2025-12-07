import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters,
    ConversationHandler, ContextTypes
)

DROPBOX_LINK, FILE_NAME = range(2)
user_data = {}

# Load template HTML
with open("dl3.html", "r", encoding="utf-8") as f:
    TEMPLATE_HTML = f.read()

# Modify Dropbox link
def modify_dropbox_link(link: str) -> str:
    if "dl=0" in link:
        return link.replace("dl=0", "dl=1")
    elif "dl=1" not in link:
        return link + "?dl=1"
    return link

# Inject link into template
def inject_link_into_template(dropbox_link: str) -> str:
    direct_link = dropbox_link.replace("www.dropbox.com", "dl.dropboxusercontent.com")
    return TEMPLATE_HTML.replace(
        "https://www.dropbox.com/scl/fi/4i0k4w918uxlirhg7rcm3/6.3.mp4?rlkey=pf1g3r8r5lbbsl4he17pv2ptb&st=cfchxo4v&dl=1",
        direct_link
    )

# Delete previous messages
async def delete_previous_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.effective_chat.id
        for msg in context.user_data.get("messages", []):
            await context.bot.delete_message(chat_id=chat_id, message_id=msg)
        context.user_data["messages"] = []
    except Exception:
        pass

# Save message ID for later deletion
async def save_message(update: Update, context: ContextTypes.DEFAULT_TYPE, msg):
    if "messages" not in context.user_data:
        context.user_data["messages"] = []
    context.user_data["messages"].append(msg.message_id)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("Send me your Dropbox shareable link:")
    await save_message(update, context, msg)
    return DROPBOX_LINK

# Handle Dropbox link (and direct messages)
async def handle_dropbox_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await delete_previous_messages(update, context)
    link = update.message.text.strip()
    if "dropbox.com" not in link:
        msg = await update.message.reply_text("❌ Please send a valid Dropbox link.")
        await save_message(update, context, msg)
        return DROPBOX_LINK

    context.user_data["link"] = modify_dropbox_link(link)
    msg = await update.message.reply_text("✅ Link accepted. Send the file name (without `.html`):")
    await save_message(update, context, msg)
    return FILE_NAME

# Handle file name
async def handle_file_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await delete_previous_messages(update, context)
    file_name = update.message.text.strip().replace(" ", "_")
    if not file_name.endswith(".html"):
        file_name += ".html"

    modified_html = inject_link_into_template(context.user_data["link"])

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(modified_html)

    await update.message.reply_document(document=open(file_name, "rb"))
    os.remove(file_name)
    return ConversationHandler.END

# Cancel command
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Cancelled.")
    return ConversationHandler.END

if __name__ == "__main__":
    BOT_TOKEN = "--"  # Replace with your bot token
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            MessageHandler(filters.TEXT & ~filters.COMMAND, handle_dropbox_link)
        ],
        states={
            DROPBOX_LINK: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_dropbox_link)],
            FILE_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_file_name)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    print("🤖 Bot started... send /start or Dropbox link directly.")
    app.run_polling()
