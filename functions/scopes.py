# scopes.py

x = 10

def my_func(a, b):
   print(x)
   print(z)

my_func(1, 2)
# z не определена, или находится вне области видимости, 
# получаем ошибку NameError.

def my_func1(a, b):
   i = 2
   print(x)

x = 10
my_func1(1, 2)

# Переменная i определена только внутри функции
# при запуске кода мы получаем ошибку NameError.

print(i)

def my_func2(a, b):
    # Переменная х внутри my_func имеет локальную область видимости функции
    # и переопределяет переменную х вне функции. 
   x = 5
   print(x)

x = 10

my_func2(1, 2)

# Когда функция завершает работу, локальная область функции my_func очищается
# область модуля содержит х=10. 

print(x)


# Оператор global объявляет переменную доступной для блока кода, следующим за оператором. 

def my_func3(a, b):
   global x
   print(x)
   x = 5
   print(x)

x = 10
my_func3(1, 2)

print(x)

# С помощью nonlocal мы можем добавлять переопределение области во внутреннюю область. 

# Тип такой функции называется closure. 
# Такая функция является блоком кода, который «закрывает» переменные nonlocal. 

def counter():
   num = 0
   def incrementer():

       # nonlocal позволяет назначать переменные во внешней области, но не в глобальной.

       nonlocal num
       num += 1
       return num
   return incrementer

c = counter()
print(c)

print(c())
print(c())
print(c())
