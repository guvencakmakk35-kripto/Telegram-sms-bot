from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
SMS_API = os.getenv("SMS_API")
SMS_KEY = os.getenv("SMS_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

def send_sms(phone, message):
    data = {
        "token": SMS_KEY,
        "phone": phone,
        "message": message
    }
    requests.post(SMS_API, json=data)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    await update.message.reply_text("SMS Bot aktif ✅")

async def sms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    try:
        phone = context.args[0]
        message = " ".join(context.args[1:])
        send_sms(phone, message)
        await update.message.reply_text("SMS gönderildi ✅")
    except:
        await update.message.reply_text("Kullanım: /sms 905xxxxxxxxx mesaj")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sms", sms))
app.run_polling()
