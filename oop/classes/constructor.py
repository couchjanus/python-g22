# constructor.py
class Person:
   def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name

# конструктор класса не позволит создать объект без обязательных полей:
sam = Person("Sam", "Brown")
print(sam.first_name, sam.last_name)


class PeculiarPerson:
   def __init__(self, first_name, last_name, favorite=1, note=''):
       self.first_name = first_name
       self.last_name = last_name
       self.favorite = favorite
       self.note = note
