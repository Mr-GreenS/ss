import time

print("\n\n=============AI-M101101 FOREVER=============\n\n")
time.sleep(2.5)

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
    

print("Стоп, нажмите любую клавишу")
input()


