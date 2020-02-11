# Что скрыто в имени
print(dir())  # ['__builtins__', '__doc__', '__name__']
directory = dir   # Создать новую переменную

print(directory()) # Работает просто как первоначальный объект ['__builtins__', '__doc__', '__name__', 'directory']
print(dir.__name__)         # Как тебя зовут? 'dir'

print(directory.__name__)   # У меня такое же имя 'dir'
print(__name__)   # '__main__'

print("__annotations__: ", __annotations__)
print("__cached__: ", __cached__)
print("__file__: ", __file__)
print("__loader__: ", __loader__)
print("__package__: ", __package__)
print("__spec__: ", __spec__)

# __annotations__:  {}
# __cached__:  None
# __file__:  name.py
# __loader__:  <_frozen_importlib_external.SourceFileLoader object at 0x7f2aa5d9f7b8>
# __package__:  None
# __spec__:  None

def main():
    directory = dir   # Создать новую переменную
    print(directory()) # Работает просто как первоначальный объект ['__builtins__', '__doc__', '__name__', 'directory']
    print(dir.__name__)         # Как тебя зовут? 'dir'
    print(directory.__name__)   # У меня такое же имя 'dir'
    print(__name__)   # '__main__'

# Определяем: выполнение или импорт
if __name__ == '__main__':
    # вызов функции main(), определенной где-то в этом модуле.
    main()
else:
    # Ничего не делать. Этот модуль был импортирован другим
    # модулем, который хочет воспользоваться этой функцией,
    # классом, которые он определил.
    pass