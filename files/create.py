my_file = open("README.md", "w")
my_file.write("# I like python! \n## It's awesome!")
my_file.close()

my_file = open("README.md", "r")
# file.name Возвращает имя файла.
print("Имя файла: ", my_file.name)
# file.mode Возвращает режим доступа, с которым был открыт файл.
print("В каком режиме файл открыт: ", my_file.mode)
my_file.close()
# file.closed Возвращает True если файл был закрыт.
print("Файл закрыт: ", my_file.closed)
