# identity() принимает аргумент x и возвращает его при вызове.

def identity(x):
    return x

# лямбда-конструкция:
# lambda x: x
# Ключевое слово: lambda
# Связанная переменная: x
# Тело: х
# связанная переменная является аргументом лямбда-функции.

# в определении lambda аргументы не имеют круглых скобок вокруг них. 
(lambda x: x + 1)(2) # 3

# Поскольку лямбда-функция является выражением, оно может быть именована:

add_one = lambda x: x + 1
add_one(2) # 3

# лямбда-функция эквивалентна:

def add_one(x):
    return x + 1



# Функции с несколькими аргументами:

# Лямбда-функция full_name, принимает два аргумента и возвращает строку, интерполирующую два параметра: 
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum') # 'Full name: Guido Van Rossum'

# передача аргументов в лямбда-выражения:

(lambda x, y, z: x + y + z)(1, 2, 3) # 6
(lambda x, y, z=3: x + y + z)(1, 2) # 6
(lambda x, y, z=3: x + y + z)(1, y=2) # 6

# Находим квадратный корень
import math

def sqroot(x):
    """
    Находим квадратный корень.
    """
    return math.sqrt(x)

square_rt = lambda x: math.sqrt(x)

print(sqroot(49)) # 7.0
print(square_rt(64)) # 8.0

(lambda x:
   (x % 2 and 'odd' or 'even'))(3) # 'odd'


# Определение lambda функции не включает оператор return - эта конструкция всегда содержит выражении, результат которого возвращается. 

# функция make_inrementor создает анонимную функцию на лету и возвращает ее. Возвращенная функция увеличивает свой аргумент на значение, которое было определенно когда она была создана.

def make_incrementor (n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print(f(42), g(42)) # 44 48

print make_incrementor(22)(33) # 55

