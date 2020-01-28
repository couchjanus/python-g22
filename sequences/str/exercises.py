# Strings are Immutable 
# Once a string is defined, it cannot be changed.
# Python3 program to show that string cannot be changed 
  
a = 'Ababahalamaha'
# output is displayed 
print(a) 
  
a[4] = 'A'
print(a) # causes error 

# Output:
# Ababahalalaha
# Traceback (most recent call last):
#   File "str/exercises.py", line 10, in <module>
#     a[4] = 'A'
# TypeError: 'str' object does not support item assignment

# Переписать программу так, чтобы она выводила
# AbabAhalAlahA
