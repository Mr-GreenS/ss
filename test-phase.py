import time
ss=input("Пожалуйста представьтесь:")
time.sleep(2.5)
ss_age = int (input("Укажите ваш возраст:"))
time.sleep(2.5)

if ss_age > 4: ss_age_s = str(ss_age) + " лет"
else: ss_age_s = str(ss_age) + " года"

print("\nДобро пожаловать " + ss +"!" + "\nИнтерфейс бота настроен на ваш возраст (т.е. " + ss_age_s + " !)")
time.sleep(2.5)
print("Мое имя AI-M101101, сокращенное AIMEE, или просто Эми")
time.sleep(2.5)
while True:
    promt_message = input("\nВаш вопрос (для выхода просто \'Эми стоп\'):")
    if len(promt_message) == 0 or promt_message == "Эми стоп": break
    print( "Обрабатываю запрос \'" + promt_message + "\' минуточку....");
    time.sleep(60)
    print( "Верю ответ найдется " + ss + " еще минуточку....");
    time.sleep(60)
    print( "К сожалению, ни локальная база знаний, ни удаленная не доступны мне сейчас," + ss + ", если хотите, введите новый запрос");
    time.sleep(2.5)
    

print("Сеанс окончен, спасибо")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
	global i_pass
	scomm=str(message.text)
	command=scomm.partition(' ')
	print(command)
	print(scomm)

	if message.text == SPASS :
		os.chdir("D:\\AIMEE")
		bot.send_message(message.chat.id, "Привет. Эми активирована.\nТекущий путь: " + os.getcwd())
		i_pass = 1
	elif i_pass == 1:
		if command[0] == "DIR":
			scomm = to_dir(message,command)
		elif command[0] == "FILE":
			print("FILE SECTION")
			print(scomm)
			scomm = to_file(message,command)
		elif command[0] == "JIRA":
			scomm = to_jira(message,command)
		elif command[0] == "Эми":
			scomm = to_aimee(message,command)
		if scomm != '' and scomm != None:
			bot.send_message(message.chat.id,scomm)
	else:
		bot.send_message(message.chat.id, "Запрос не распознан")
