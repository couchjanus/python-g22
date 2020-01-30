# Strings are Immutable 
# Once a string is defined, it cannot be changed.
# Python3 program to show that string cannot be changed 
  
a = 'ababahalamalah'

# output is displayed 
print(a) 

# Output:
# Ababahalalaha
# Traceback (most recent call last):
#   File "str/exercises.py", line 10, in <module>
#     a[4] = 'A'
# TypeError: 'str' object does not support item assignment

# Переписать программу так, чтобы она выводила
# AbabAhalAlahA

def chageCap(x, y):
    z = ''
    for i in x.lower():
        if i.find(y.lower()) == -1:
            z +=i
        else:
            z +=i.swapcase()
    return z

def isPalindrome(s): 
    rev = ''.join(reversed(s)) 
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
# main function 

# print("Yes") if isPalindrome(a) else print("No")  
# print("Yes") if isPalindrome(b) else print("No")  

print(chageCap(a[0:a.find('h')], a[0:1])+chageCap(a[a.find('h'):], a[0:1]))

