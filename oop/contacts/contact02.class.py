# contact02.class.py
'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
# Importing libraries
from datetime import datetime
import pickle

FILENAME = "contacts.dat"

data = []

choices = {'a':'Add contact', 'p': "Print Contacts", 'q': "Quit", 'h': "Help"}

class Person:
    """ Class Documentation """

    def __init__(self, first_name, last_name):
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
            
            for contact in data:
                print(f"Имя: {contact['first_name']} {contact['last_name']} \tOffice phone: {contact['office']} \tAdded At: {contact['date']} :{contact['time']}")

    if choice == 'a':
        print("Add New Record To PhoneBook")

        first_name = input("First Name: ")
        last_name = input("Last Name: ") 
        office_phone = input("Office Phone Number: ")

        person = Person(first_name, last_name)
        person.add_office_phone(office_phone)

        person.save(person.__dict__, FILENAME)
