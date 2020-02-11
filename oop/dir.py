# Имена в текущей области: dir()
print(type(dir)) # <type 'builtin_function_or_method'>
print("Имена в текущей области")
print(dir())

# Атрибуты модуля __builtins__
print("Атрибуты модуля __builtins__")
print(dir(__builtins__))

# Атрибуты модуля keyword
# import keyword

# print("Атрибуты модуля keyword")
# print(dir(keyword))

# print(dir(keyword.__all__))
# print(dir(keyword.__builtins__))
# print(dir(keyword.kwlist))


# Атрибуты модуля math
import math

print(dir(math))

print(math.__doc__) 
# This module is always available.  It provides access to the
# mathematical functions defined by the C standard.

print(math.pow.__doc__)
# Return x**y (x to the power of y).

# Here we see an output of the dir() function for a tuple object.

print(().__doc__)

# Built-in immutable sequence.

# If no argument is given, the constructor returns an empty tuple.
# If iterable is specified the tuple is initialized from iterable's items.

# If the argument is a tuple, the return value is the same object.
