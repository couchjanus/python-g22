# Создать List comprehension version
cart_1 = [1, 8, 29, 34, 58, 74, 88, 99]
cart_2 = [3, 8, 31, 36, 58, 77, 88, 93]
# Создать cashier_3, содержащий одновременно 2 одинаковых элемента
# Non-list comprehension version
cashier_3 = []
for item in cart_1:
   if item in cart_2:
       cashier_3.append(item)
print(cashier_3) # Out:[8, 58, 88]


# List comprehension version
cashier_4 = [item for item in cart_1 if item in cart_2]
print(cashier_4) # Out:[8, 58, 88]
