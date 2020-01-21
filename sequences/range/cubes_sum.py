# cubes sum

n = int(input("Enter number: "))
sum = 0
for i in range(n + 1):
   a = i ** 3
   sum += a
print('cubes sum: ', sum)
