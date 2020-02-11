class B:
   """Определения атрибутов класса"""

   attribute1 = 2

b = B()
# Интроспекция
print(b.__class__) # <class '__main__.B'>
print(B.__dict__) # {'__module__': '__main__', '__doc__': 'определение класса', 'attribute1': 2, '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>}
print(b.__dict__) # {}


class C:
   """Определение метода класса"""

   attribute1 = 2

   def my_method(self, x):
      # блок кода метода
      pass

c = C()
# Интроспекция
print(c.__class__) # <class '__main__.C'>
print(C.__dict__) # {'__module__': '__main__', '__doc__': 'Определение метода класса', 'attribute1': 2, 'my_method': <function C.my_method at 0x7f10c0e8fea0>, '__dict__': <attribute '__dict__' of 'C' objects>, '__weakref__': <attribute '__weakref__' of 'C' objects>}

print(c.__dict__) # {}


class D:
   """Определение класса"""

   attribute_for_d = 2

   def my_method(self, x):
      print(x)

d = D()
print(d.attribute_for_d)
print(d.my_method("Hello D class"))

# Интроспекция

print(d.__dict__) # {}
print(dir(d)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_for_d', 'my_method']


def my_method1(self, x):
  return x * x

D.m1 = my_method1
D.attr1 = 2 * 2
d1 = D()

print(d1.attribute_for_d)
print(d1.attr1)
print(d1.m1(4))

print(dir(d1)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attr1', 'attribute_for_d', 'm1', 'my_method']
