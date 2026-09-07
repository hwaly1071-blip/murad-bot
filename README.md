import os
import telebot

# ياخذ التوكن من Koyeb Secrets - آمن 100%
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise Exception("حط التوكن الجديد في Koyeb > Environment!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello Murad! 🔥\nالبوت شغال 24 ساعة على Koyeb!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"استلمت: {message.text}")

print("Bot started polling...")
bot.infinity_polling()
