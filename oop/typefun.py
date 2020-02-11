# typefun.py

print(type(1))
print(type(""))
print(type([]))
print(type({}))
print(type(()))
print(type(object))

def function():
    pass

# The type() function returns the type of an object.
print(type(function))

# isinstance():

print(isinstance(42, str))
print(isinstance('a string', int))

print(isinstance(42, int))
print(isinstance('a string', str))
