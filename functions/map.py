# функция filter() фильтрует все четные числа в данном списке целых чисел:

even = lambda x: x%2 == 0
list(filter(even, range(11))) # [0, 2, 4, 6, 8, 10]

# Реализация, использующая конструкцию генератора списка:

[x for x in range(11) if x%2 == 0] # [0, 2, 4, 6, 8, 10]


# алгоритм решето Эратосфена 
# один из путей вычислений простых чисел:

nums = range(2, 50)

# инициализируем список nums числами от 2 до 49. 
# цикл for проходит по всем возможным делителям, т.е. значение i проходит от 2 до 7. 
# все числа что кратны этим делителям не могут быть простыми числами, 
# мы используем функцию filter() для удаления их из списка.

for i in range(2, 8):
    nums = filter(lambda x: x == i or x % i, nums)

print(list(nums)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# функция filter() указывает: оставить элемент в списке если он равен i или если остается не нулевой остаток при делении на i. Иначе удалить его из списка. После того как фильтрующий цикл закончиться останутся только простые числа. 


foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

# filter() вызывает lambda функцию для каждого элемента списка и возвращает новый список, который содержит только те элементы для которых функция возвращает “true”. В этом случае, мы получаем список всех элементов которые кратные 3. Выражение x % 3 == 0 вычисляет остаток от деления x на 3 и сравнивает результат с 0 (которые равняется true если х делиться ровно на 3).

print(list(filter(lambda x: x % 3 == 0, foo))) # [18, 9, 24, 12, 27]

print(list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))) # ['dog', 'cow']


# функция map() используется для преобразования списка. В этом случаи вычисляется 2 * x + 10 для каждого элемента.

print(list(map(lambda x: x * 2 + 10, foo))) # [14, 46, 28, 54, 44, 58, 26, 34, 64]

print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))) # ['CAT', 'DOG', 'COW']

# предложение разбивается на список слов, затем создается список который содержит длину каждого слова.

sentence = 'It is raining cats and dogs'
words = sentence.split()
print(words) # ['It', 'is', 'raining', 'cats', 'and', 'dogs']

lengths = map(lambda word: len(word), words)
print(list(lengths)) # [2, 2, 7, 4, 3, 4]

import functools

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# Чтобы применить reduce() к списку пар и вычислить сумму первого элемента каждой пары:

functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0) # 6

# идиоматический подход, использующий выражение генератора в качестве аргумента для sum():

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
sum(x[0] for x in pairs) # 6

# Функция reduce() должна принимать два аргумента (x и y). Функция вызывается для первых двух элементов из списка, затем для результата предыдущих вычислений и третего и т.д. пока не будут обработаны все элементы списка. Это означает, что функция будет вызвана n-1 раз если список содержит n элементов. Возвращенное значение последнего вызова есть результат операции reduce(). В выше приведенном примере просто суммируются аргументы.

from functools import reduce

print(reduce(lambda x, y: x + y, foo)) # 139

print(reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])) #'cat | dog | cow'

# Лямбда-функция может быть функцией более высокого порядка, 
# принимая функцию (нормальную или лямбда-функцию) в качестве аргумента:

high_ord_func = lambda x, func: x + func(x)

print(high_ord_func(2, lambda x: x * x)) # 6
print(high_ord_func(2, lambda x: x + 3)) # 7