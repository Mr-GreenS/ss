import time
import telebot
import os

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
		bot.send_message(message.chat.id, "Привет. Исходная:" + os.getcwd())
		i_pass = 1
	elif i_pass == 1:
		if message.text == "DIR":
			print("Запрос DIR:", os.listdir());				
			bot.send_message(message.chat.id,os.listdir())
			# распечатать все файлы и папки рекурсивно
			#for dirpath, dirnames, filenames in os.walk("."):
				# перебрать каталоги
				#for dirname in dirnames:
				#	bot.send_message(message.chat.id,"Каталог:" + os.path.join(dirpath, dirname))
				# перебрать файлы
				#for filename in filenames:
				#	bot.send_message(message.chat.id,"Файл:" + os.path.join(dirpath, filename))
		else:
			os.mkdir(message.text)
			bot.send_message(message.chat.id, "Создана директория:" + message.text)
			time.sleep(20)
			bot.stop_bot()

	else:
		bot.send_message(message.chat.id, "Запрос не распознан")
bot.polling(none_stop = True)


time.sleep(2.5)




