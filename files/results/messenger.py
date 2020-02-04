# Exercise 2  messenger.py

# Создать скрипт, который записывает введенное пользователем сообщение в файл
# и выводит его обратно из файла на консоль:

# имя файла FILENAME = "messenges.txt"
# Введите сообщение
# запись сообщения в файл
# Все сообщения из файла


# имя файла
FILENAME = "messenger.txt"
# определяем пустой список
messages = list()
 
for i in range(4):
    message = input("Введите строку " + str(i+1) + ": ")
    messages.append(message + "\n")
 
# запись списка в файл
with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)
 
# считываем сообщения из файла
print("Считанные сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message)
