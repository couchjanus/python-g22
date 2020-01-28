# В диапозоне range(10) выведите сумму текущего номера и предыдущего номера
# Ожидаемый результат:
 0
 1
 3
 5
 7
 9
 11
 13
 15
 17


def sumNum(num):
  previousNum=0
  for i in range(num):
    sum = previousNum + i
    print(sum)
    previousNum = i

print("Printing current and previous number sum in a given range")
sumNum(10)
