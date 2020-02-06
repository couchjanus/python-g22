# Exercise 1
  
# Есть csv file
# filename = "users.csv"

# name,age
# Tom,28
# Alice,23
# Mary,18
# Ann,20
# Bob,34
# Sam,41
# прочитать csv file 
# Извлечь заголовки полей из первой строки 
# Извлечь данные начиная со 2-й строки
# Напечатать общее число строк
# Напечатать имена полей
# Напечатать первые 5 строк 

# importing csv module 
import csv 
  
# csv file name 
filename = "users.csv"
  
# init titles и rows
fields = [] 
rows = [] 
  
# прочитать csv file 
with open(filename, 'r') as csvfile: 
    # слздаем csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # Извлечь заголовки полей из первой строки 
    fields = next(csvreader)
  
    # Извлечь данные начиная со 2-й строки
    for row in csvreader: 
        rows.append(row) 
  
    # Напечатать общее число строк
    print(f"Total no. of rows: {csvreader.line_num}") 
  
# Напечатать имена полей
print('Field names are:' + ', '.join(field for field in fields)) 
  
#  Напечатать первые 5 строк 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
    # итерация по каждому column в row 
    for col in row: 
        print("%10s"%col), 
    print('\n') 
