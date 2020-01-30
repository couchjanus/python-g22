# Читаем файл myfile.txt:
my_file = open("myfile.txt")
my_string = my_file.read()
print("Было прочитано:")
print(my_string)
my_file.close()

# Файл сам может выступать в роли итератора:

for line in open('hello.txt'):
    print(line)



