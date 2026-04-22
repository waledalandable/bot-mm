import telebot
from config import BOT_TOKEN
from handlers import register

bot = telebot.TeleBot(BOT_TOKEN)

register(bot)

print("Bot running...")
bot.infinity_polling()
