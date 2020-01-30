def menu():
    return input('{}'.format("\nEnter something like Hello or q : "))

# while True:
#     file = open("myfile.txt", 'w') # w, a, w+, a+, wb, wb+, ab, ab+
#     enter = menu()
    
#     if enter == 'q':
#         file.close()
#         print('{!s}'.format('Thank You for using writer.py!'))
#         break
#     else:
#         # file.write(enter) # Writing to file
#         file.write(enter.encode())


# hello_file = open("hello.txt", "a")
# print("Hello, world", file=hello_file)
# hello_file.close()
    
# # Creating a file  
# file1 = open("hello.txt", "w")  
# L = ["Welcome to Kyiv \n", "Welcome to Paris \n", "Welcome to Hlevakha \n"]  
    
# # Writing data to a file  
# file1.write("Hello \n")   
# file1.writelines(L)  
# file1.close()  # to change file access modes  


with open("hello.txt", "w") as file:
   file.write("hello world")
# Теперь пишем в этот файл еще одну строку:
with open("hello.txt", "a") as file:
   file.write("\ngood bye, world")

with open("hello.txt", "a") as hello_file:
   print("Hello, world", file=hello_file)


# save dictionary to text file (raw, .txt)

dic = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
f = open("dict.txt", "w")
# каждая запись словаря находится на отдельной строке:
for item in dic.items():
    print(item)
    f.write(str(item)+"\n")
f.close()

# Чтение из словаря с помощью eval.
# это будет работать, если каждая запись словаря находится на отдельной строке:

dicts_from_file = [] 
with open('dict.txt','r') as item:
    for line in item: 
        dicts_from_file.append(eval(line)) 

print(dicts_from_file)
# Преобразование в словарь
d = dict(dicts_from_file)
print(d)
print(type(d))

# Запись словаря в файл с разделителем
dic1 = {
    "name":'Mary Ann',
    "age":'22',
    "phone":'1234567'
}

file = open("dicfile.txt","w")
for k,v in dic1.items():
    file.write(f'{k}*{v}\n')
file.close()

# Чтение из словаря с использованием split
dic_1 = {}

file=open("dicfile.txt","r")
for i in file.readlines():
    data = i.strip().split('*')
    dic_1[data[0]] = ''.join(data[1:])
print(dic_1)

# Чтение из словаря с использованием with и split
d = {}
with open('dicfile.txt') as file:
    for i in file.readlines():
        key,val = i.strip().split('*')
        d[key] = val
print(d)

