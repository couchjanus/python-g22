# Наличие атрибута; получение атрибута

print(hasattr.__doc__)
# Return whether the object has an attribute with the given name.
# This is done by calling getattr(obj, name) and catching AttributeError.

print("Наличие атрибута: ", hasattr(object, 'name'))
# Наличие атрибута:  False

print(getattr.__doc__)
# getattr(object, name[, default]) -> value

# Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
# When a default argument is given, it is returned when the attribute doesn't
# exist; without it, an exception is raised in that case.

print("Наличие атрибута id: ", hasattr(id, '__doc__'))
# Return the identity of an object.
print(getattr(id, '__doc__'))
# This is guaranteed to be unique among simultaneously existing objects.
# (CPython uses the object's memory address.)

print("получение атрибута: ", id(object))
# 94044935661312

alist = [1, 2, 3]
blist = [1, 2, 3]

clist = blist 

print(clist) # [1, 2, 3]
print(blist) # [1, 2, 3]
print(alist) # [1, 2, 3]

print(id(alist)) # 145381412
print(id(blist)) # 140406428
print(id(clist)) # 140406428

print(alist is blist) # False
print(blist is clist) # True

clist.append(4) # Добавить элемент в конец списка
print(clist) # [1, 2, 3, 4]
print(blist) # [1, 2, 3, 4], поскольку они обе указывают на один и тот же объект [1, 2, 3, 4]
print(alist) # [1, 2, 3]
