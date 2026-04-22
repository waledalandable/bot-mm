import telebot
from config import BOT_TOKEN
from handlers import register
from keep_alive import keep_alive

bot = telebot.TeleBot(BOT_TOKEN)

register(bot)

keep_alive()

print("Bot running...")
bot.infinity_polling()