# Python range() Function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# range(start, stop, step)
# Parameter Values
# start 	Optional. An integer number specifying at which position to start. Default is 0
# stop 	Required. An integer number specifying at which position to end.
# step 	Optional. An integer number specifying the incrementation. Default is 1

# Using only one argument in range()
# Only stop argument is passed to range() function.
# So by default, it takes start = 0 and step = 1.

# Create a sequence of numbers from 0 to 5, and print each item in the sequence:
x = range(6)

# цикл выполняет блок кода или оператора фиксированное количество раз. 
# Используя цикл for, мы можем перебрать последовательность чисел, созданную функцией range().

# for n in x:
#   print(n)

# переменная n получает значения 0, 1, 2, 3, 4, 5 не одновременно. а последовательно. то есть в первой итерации n = 0. во второй итерации n становится 1 и так далее.




##############################
# print numbers from range 0 to 6: 0, 1, 2, 3, 4, 5,
# print("Python range() example to print numbers from range 0 to 6")
# for i in range(6):
#     print(i, end=', ')

# using two arguments (i.e., start and stop) in range() function
# Only two arguments (the start and stop) are passed to the range function.
# So by default, it took step argument value as 1.

##############################
# Create a sequence of numbers from 3 to 5, and print each item in the sequence:
# x = range(3, 6)
# for n in x:
#   print(n)


##############################
# Print integers within given start and stop number using range() function 5, 6, 7, 8, 9,

# print("Print integers within given start and stop number using range() function")
# for i in range(5, 10):
#     print(i, end=', ')

# range(начало, конец) не включает конец потому что индекс в python всегда начинается с нуля. если вы посчитаете общее число в range(5), вы получите [0,1,2,3,4], т.е. общее количество равно 5.

# list(range(5))
# list(range(0))  # []
# list(range(1, 0))  # []














##############################
# using all three arguments in range() function
# using start, stop, and step arguments in Python range() function

# Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
# x = range(3, 20, 2)
# for n in x:
#   print(n) 

# Printing All odd numbers between 1 and 10 using range(): 1, 3, 5, 7, 9,
# All three arguments are specified. i.e. start = 1, stop = 10, step = 2.

# print("using start, stop, and step arguments in Python range() function")
# print("Printing All odd numbers between 1 and 10 using range()")
# for i in range(1, 10, 2):
#     print(i, end=', ')














##############################
# Python range inclusive
# range(n) не включает в себя последнее число в выводе. т.е. данная конечная точка никогда не является частью сгенерированного результата.
# Например, range(0, 5) = [0,1,2,3,4]. То есть он генерирует целые числа от 0 до 5, но не включает 5. Если вы хотите включить последнее число в вывод, передайте значение аргумента stop как stop + step.

# print("Printing inclusive range")
# start = 1
# stop  = 5 
# step  = 1
# # to get inclusive range change stop as stop+step
# stop +=step #now stop is 6

# for i in range(start, stop, step):
#     print(i, end=', ')

# Printing inclusive range 1, 2, 3, 4, 5,

##############################
# Inclusive range

# print("Printing inclusive range")
# start = 2
# stop  = 10 
# step  = 2
# # to get inclusive range change stop as stop+step
# stop +=step #now stop is 12

# for i in range(start, stop, step):
#     print(i, end=', ')

# Printing inclusive range 2, 4, 6, 8, 10,












########### Python range Step ###########

# Шаг является необязательным аргументом в функции range. Шаг представляет собой разницу между каждым числом в последовательности. Размер шага по умолчанию равен 1, если не указан. Если размер шага равен 2, то разница между каждым числом равна 2.

# Мы можем выполнять множество операций, эффективно используя аргументы шага, такие как изменение последовательности, печать отрицательных диапазонов.

# list(range(0, -5, -1))  # [0, -1, -2, -3, -4]
##############################
# Уменьшение с помощью range() с использованием отрицательного шага
# Мы можем использовать отрицательные значения во всех аргументах функции range(), то есть start, stop и step.

# start = -2
# stop = -10
# step = -2
# print("Negative number range")
# for number in range(start, stop, step):
#     print(number, end=', ')

# Negative number range -2, -4, -6, -8,

# we set, start = -2stop = -10, step = -2.
# in the 1st iteration of for loop  = [-2].
# in the 2nd iteration of for loop = [-2,-4]  because -2+(-2) == -4 and so on
# and Last iteration output is [-2,-4,-6,-8]




##############################
# Decrementing with the range from Negative to Positive number
# how to use step argument to display a range of numbers from negative to positive.

# print ("printing range from negative to positive")
# for num in range(-2,5,1):
#     print(num, end=", ")

# The output of the above program
# printing range from negative to positive -2, -1, 0, 1, 2, 3, 4,
##############################
# range от положительного до отрицательного числа
# print (" printing range from Positive to Negative")
# for num in range(2,-5,-1):
#     print(num, end=", ")
# printing range from Positive to Negative 2, 1, 0, -1, -2, -3, -4,











########### Convert Python range() to List ###########
# Функция range() возвращает неизменяемый объект последовательности целых чисел, поэтому можно преобразовать выходные данные range() в список Python. Используйте класс списка для преобразования вывода диапазона в список. 

# print("Converting python range() to list")
# even_list = list( range(2,10,2))
# print("printing list", even_list)
# Converting python range() to list printing list [2, 4, 6, 8]








########### Обратный range ###########
# напечатать последовательность чисел [5,4,3,2,1] в обратном порядке.
# Используйте отрицательное значение шага. 

# print ("Displaying list of numbers by reverse order using range()")
# for number in range(4,-1,-1):
#     print (number, end=', ')
# Displaying list of numbers by reverse order using range() 4, 3, 2, 1, 0
