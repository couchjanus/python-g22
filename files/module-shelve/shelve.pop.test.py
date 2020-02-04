# shelve.pop.file.test.py
import shelve

FILENAME = "states" 

with shelve.open(FILENAME) as states:
    state = states.pop("London", "NotFound")
    print(state)

# Также для удаления может применяться оператор del:
with shelve.open(FILENAME) as states:
    del states["Madrid"]    # удаляем объект с ключом Madrid

# Для удаления всех элементов можно использовать метод clear():

with shelve.open(FILENAME) as states:
    states.clear()

