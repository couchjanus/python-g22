# Exercise 3 

# Задан словарь
dic1 = {
    "name":'Mary Ann',
    "age":'22',
    "phone":'1234567'
}

# Напишите функцию записи словаря в файл
# Функция должна принимать в качестве параметра словарь

# Напишите функцию чтения словаря из файла
# Функция должна возвращать словарь из файла

# {'name': 'Mary Ann', 'age': '22', 'phone': '1234567'}
# <class 'dict'>
# save_load_dict.py
def save_dict_to_file(dic):
    f = open('dict.txt','w')
    f.write(str(dic))
    f.close()

def load_dict_from_file():
    f = open('dict.txt','r')
    data=f.read()
    f.close()
    return eval(data)

# Запись словаря в файл с разделителем
dic1 = {
    "name":'Mary Ann',
    "age":'22',
    "phone":'1234567'
}

save_dict_to_file(dic1)
print(load_dict_from_file())

print(type(load_dict_from_file()))