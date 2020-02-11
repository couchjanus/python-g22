# contact01.class.py
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
