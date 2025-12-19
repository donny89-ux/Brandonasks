from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os

# Load keys from environment
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def start(update, context):
    update.message.reply_text("Hi, I'm BrandonAsks 🤖. Ask me anything!")

def chat(update, context):
    user_text = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are BrandonAsks, a helpful AI chatbot."},
            {"role": "user", "content": user_text}
        ]
    )
    update.message.reply_text(response.choices[0].message["content"])

updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

updater.start_polling()
updater.idle()
