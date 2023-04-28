import time
import telebot
i_pass= 0
SPASS= "Aimee"

bot = telebot.TeleBot("6065910250:AAEJ0P0eFCP3rmr5S6WLw0452LuJxDgKlt4", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "\n\n=======AI-M101101 FOREVER=======\n\n")
	bot.send_message(message.chat.id, "\n\nВведите пароль\n\n")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, "\n\nЗапрос = имя файла/текст\n\n")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
	global i_pass
	if message.text == SPASS :
		bot.send_message(message.chat.id, "Привет")
		i_pass = 1
	elif i_pass == 1:
		bot.send_message(message.chat.id, message.text)
	else:
		bot.send_message(message.chat.id, "Запрос не распознан")
bot.polling(none_stop = True)


time.sleep(2.5)




