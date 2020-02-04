import os

# Значение os.name. 
print(os.name) # posix

# Значение os.environ
# os.environ, os.getenv() и os.putenv()
# print(os.environ)
print(os.environ["USER"])  
print(os.getenv("USER"))
print(os.getenv("LANG"))

# Узнать текущий каталог:
print(os.getcwd())

# Смена текущего каталога:
# os.chdir('/home')
# print(os.getcwd())

# Создать каталог:
# os.mkdir('dir1')
# path = r'C:\Users\mike\Documents\pytest'
# path = r'C:\temp\pytest'
# os.mkdir(path)

# Создать дерево каталогов:
# os.makedirs('one/tow/three')
# os.remove("C://SomeDir/hello.txt")
# Список содержимого каталога (нерекурсивный):
# print(os.listdir('one')) # ['tow']
# print(os.listdir('one/tow')) # ['three']

# print(os.listdir())
# print(os.listdir('/home'))

# Сведения о файле|каталоге:
# print(os.stat('/home'))
# print(os.stat('main.py'))

# with open("test.txt", 'w') as h:
#     h.write("Test text")

# print(os.stat('test.txt'))

# with open("test.txt", 'w') as h:
#     h.write("Test text")
# print(os.stat('test.txt'))

# Переименовать файл:
# os.rename('test.txt', 'test1.txt')
# print(os.stat('test1.txt'))

# Переименовать каталог:
# os.rename('dir1', 'dir2')

# Удаление файла|каталога:
# os.remove("test.txt")
# os.rmdir('dir2')
