# Есть список из 5 чисел: [3, 6, 9, 12, 15],
# отобразить каждый элемент, удвоив его с помощью функции for loop и range():

# Element Index[ 0 ] Previous Value  3 Now  6
# Element Index[ 1 ] Previous Value  6 Now  12
# Element Index[ 2 ] Previous Value  9 Now  18
# Element Index[ 3 ] Previous Value  12 Now  24
# Element Index[ 4 ] Previous Value  15 Now  30

print("Double the list numbers using for loop and range() function")

sampleList = [3, 6, 9, 12, 15]

# используя len(list), мы получили общее количество элементов списка, поэтому мы можем повторять цикл len(list) раз.

# В каждой итерации с помощью функции range() цикл получает индекс текущего элемента.

for i in range(len(sampleList)):
    print( "Element Index[", i, "]", "Previous Value ", sampleList[i], "Now ", sampleList[i] * 2)
