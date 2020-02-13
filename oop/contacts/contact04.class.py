# contact04.class.py
'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
# Importing libraries
from datetime import datetime
import pickle
from collections import namedtuple

FILENAME = "contacts.dat"

data = []

choices = {'a':'Add contact', 'p': "Print Contacts", 'q': "Quit", 'h': "Help"}


class AttributeDict(dict):
    def __getattr__(self, name):
        return self[name]

class Person:
    """ Class Documentation """

    def __init__(self, first_name='', last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = None
        self.office = None
        self.__private = None
        self.email = None
        self.address = None
        self.age = None
        self.date = self.__current_date()[0]
        self.time = self.__current_date()[1]
    
    def full_name(self):
        return self.first_name.title() +" " + self.last_name.title()

    def add_mobile_phone(self, number):
        """ Method documentation """
        
        self.mobile = number

    def add_office_phone(self, number):
        self.office = number

    def add_email(self, email):
        self.email = email

    def __current_date(self):
        now = datetime.now()
        day = now.day
        month = now.month
        year = now.year
        hour = now.hour
        minute = now.minute
        second = now.second
        return [f'{day}/{month}/{year}', f'{hour}:{minute}:{second}']

    def add_private_phone(self, number):
       self.__private = number

    def get_private_phone(self):
        try:
            return self.__private
        except:
            return False

    def save(self, obj, filename):
        with open(filename, 'ab') as file:
            pickle.dump(obj, file)

def cHelp(e=''):
    print(f"\n{e}") if e != '' else print()
    print ("""
        Usage operation:
            h                    Display this usage message
            a                    Add
            p                    Print
            q                    Quit
        """)

def menu():
    print(f"Contacts".title().center(30, '='), '\n')
    choice = input("| Enter choice (" + ''.join(((i+'|') for i in choices.keys()))+"):")
    
    return str(choice.lower()) if choice.lower() != '' else 'h'


while True:
    choice = menu()

    if choice == 'q':
        print('{!s}'.format('Thank You for using contact!'))
        break 
    
    if choice == 'h':
        cHelp()
        continue

    if choice == 'p':
        
        with open(FILENAME, "rb") as file:
            try:
                while True:
                    data.append(pickle.load(file))
            except EOFError:
                pass
            
            person = Person()

            for contact in data:
                person = AttributeDict(contact)
                print(f"Имя: {person.first_name} {person.last_name} \tPhone: {person.office} \tDate: {person.date} :{person.time} \tPrivate: {person._Person__private}")

    if choice == 'a':
        print("Add New Record To PhoneBook")

        first_name = input("First Name: ")
        last_name = input("Last Name: ") 
        office_phone = input("Office Phone Number: ")
        
        person = Person(first_name, last_name)
        person.add_office_phone(office_phone)
        
        private = input("Have a private phone? (y|n): ")

        if (private == 'y'):
            private_phone = input("Private Phone Number: ")
            person.add_private_phone(private_phone)

        person.save(person.__dict__, FILENAME)
