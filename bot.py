import telebot
TOKEN="8987342278:AAFz63RW4P_4envV0pvkqe-Ux1kArxkgnmk"
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,"Hello Murad! Bot is online 24h 🔥")

bot.infinity_polling()
