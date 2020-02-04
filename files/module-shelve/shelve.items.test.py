# shelve.items.file.test.py

# можно открывать файл с помощью оператора with. 
# Сохраним и считаем в файл несколько объектов:
import shelve
 
FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

# метод items() возвращает набор кортежей. 
# Каждый кортеж содержит ключ и значение.

with shelve.open(FILENAME) as states:
 
    for state in states.items():
        print(state)
