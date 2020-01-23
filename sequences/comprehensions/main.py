# comprehension

# Given list
# list = [10, 20, 30, 40, 50, 60, 70]

# for elem in list:
#     elem = elem + 5
#     print(elem)

##############################
# создать список, который содержит квадраты всех чисел от 1 до 9:

# list_of_squares = []
# for int in range(1, 10):
#     square = int ** 2
#     list_of_squares.append(square)
# print(list_of_squares)
# List_of_squares с помощью цикла: [1, 4, 9, 16, 25, 36, 49, 64, 81]

##############################
# Given list
# list = [5, 7, 9, 10, 12, 15, 19, 20, 22] 

# Make a new list even_list with even numbers
# even_list = []

# for item in list:
#     if item % 2 == 0:
#         even_list.append(item)
# print(even_list)
# the output is only the even numbers: [10, 12, 20, 22]













##############################
# list = [10, 20, 30, 40, 50, 60, 70]

# res = [x + 5 for x in list]
# print(res)
# [15, 25, 35, 45, 55, 65, 75]

##############################

# Non-list comprehension
# a = []
# for i in range(100):
#     a.append(i)
# print(a)

# # List comprehension version
# b = [i for i in range(100)]
# print(b)

# res = [x for x in range(1, 25, 2)]
# print(res)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]








##############################
# создать список, который содержит квадраты всех чисел от 1 до 9:

# list_of_squares = [int**2 for int in range(1, 10)]
# print('List of squares using list comprehension: {}'.format(list_of_squares))

# Вывод с помощью конструктора: [1, 4, 9, 16, 25, 36, 49, 64, 81]












##############################

# Given list
list = [5, 7, 9, 10, 12, 15, 19, 20, 22] 
# Make a new list even_list with even numbers

# Pass items to even_list but with a list comprehension

# even_list = [item for item in list]
# print(even_list)
# Output: [3, 4, 12, 17, 19, 21, 23, 26, 30]









##############################

# Условные выражения
# Чётные числа от 2 до 9998 включительно:
# res = [n for n in range(1, 10000) if n % 2 == 0]
# print(res)

# исключались квадраты чисел, кратных 3.
# res = [x**2 for x in range(1, 25, 2) if x % 3 != 0]
# print(res)
# [1, 25, 49, 121, 169, 289, 361, 529]








##############################
# Условные выражения позволяют отфильтровывать нежелательные значения:
# sentence = 'the rocket came back from mars'
# условный оператор отфильтровывает любые символы в sentence, которые не являются гласными.
# vowels = [i for i in sentence if i in 'aeiou']
# print(vowels)
# ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']








##############################
# Условие может содержать любое допустимое выражение. Если вам нужен более сложный фильтр, вы можете даже переместить условную логику в отдельную функцию:

# sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'

# def is_consonant(letter):
#     vowels = 'aeiou'
#     return letter.isalpha() and letter.lower() not in vowels

# consonants = [i for i in sentence if is_consonant(i)]
# print(consonants)








##############################

# Если вы хотите изменить значение элемента вместо его фильтрации, можно поместить условное выражение в начале выражения:
# new_list = [expression (if conditional) for member in iterable]
# С помощью этого шаблона можно использовать условную логику для выбора из нескольких возможных вариантов вывода. 
# Например, если есть список цен, можно заменить отрицательные цены на 0 и оставить положительные значения без изменений:

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# prices = [i if i > 0 else 0 for i in original_prices]
# print(prices)
# [1.25, 0, 10.22, 3.78, 0, 1.16]

# Выражение i содержит условный оператор, if i> 0 else 0. Это позволяет выводить значение i, если число положительное, но менять i на 0, если число отрицательное. 







##############################
# Можно переместить условную логику в отдельную функцию:

# def get_price(price):
#     return price if price > 0 else 0
# prices = [get_price(i) for i in original_prices]
# print(prices)
# [1.25, 0, 10.22, 3.78, 0, 1.16]













##############################
# Списковые включения могут использовать вложенные итерации по переменным:
# res = [(x, y) for x in range(1, 10) for y in range(1, 10) if x % y == 0]
# print(res)