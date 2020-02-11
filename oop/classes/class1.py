# Минимально возможное определение класса:
class A(object):
   """Минимально возможное определение класса"""

   pass

# print(type(A))# <class 'type'>

# Интроспекция

# print(dir(A)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# print(A.__dict__) # {'__module__': '__main__', '__doc__': 'Минимально возможное определение класса', '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>}

# print(A.__doc__) # Минимально возможное определение класса

# type и object - это объекты. 
# как у всех объектов, у них есть специальные атрибуты __class__ и __dict__:

# print(object.__class__) # <class 'type'>
# print(type.__class__) # <class 'type'>
# print(A.__class__) # <class 'type'>

# print(object.__dict__) 
# print(type.__dict__) 
# print(A.__dict__)  

# object, и type — это объекты типа (классы), 
# и у них тоже есть специальные атрибуты __name__, __bases___:

# print(object.__name__) # 'object'
# print(type.__name__) # 'type'
# print(object.__bases__) # ()
# print(type.__bases__) # (<type 'object'>,)

# print(A.__name__) # 'object'
# print(A.__bases__) # ()


# Интроспекция

# Экземпляры типа или класса object - это объекты
# Т.е. любой объект — экземпляр класса object:

# print(isinstance(1, object)) # True
# print(isinstance(setattr, object)) # True
# print(isinstance("foo", object)) # True
# print(isinstance(A, object)) # True

# функция является объектом:
def bar():
    pass

isinstance(bar, object) #True

# класс object сам является своим экземпляром:
isinstance(object, object) # True

# type тоже является его экземпляром:
isinstance(type, object) # True

# Инстанцирование 

# object() возвращает самый простой и общий объект:
o = object()

# У object нет __dict__ нет, 
o.__dict__

# есть только __class__
o.__class__ # <type 'object'>

# Экземпляры класса или типа type — это только другие классы или другие типы:

# Число — это не класс
isinstance(1, type) # False

# Строка тоже
isinstance("foo", type) # False

# Встроенная функция setattr тоже не класс.
isinstance(setattr, type) # False

# Класс — это класс. 
isinstance(A, type) # True

# Тип строки — это класс.
isinstance("foo".__class__, type) # True

# Т.к. object и type — тоже классы, то они являются экземплярами класса type:
isinstance(object, type) # True
isinstance(type, type) # True

# Т.к. множество классов (типов) являются подмножеством множества объектов, 
# то type является подклассом object, т.е.
issubclass(type, object) # True
issubclass(object, type) # False

# type — это просто класс, экземплярами которого являются другие классы. 
# А сами классы можно считать расширением простых, обычных объектов.

# a = A()
# # print(dir(a)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# print(a.__class__) # <class '__main__.A'>
# print(a.__dict__) # {}
