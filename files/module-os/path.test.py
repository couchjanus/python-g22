import os

# os.path.abspath(path)
# возвращает полный путь до папки/файла
# print(os.path.abspath("main.py"))

# os.path.basename(path)
# path (str) – путь к файлу/папке
# Возвращает строку, имя файла или папки.
# print(os.path.basename("./main.py"))

# os.path.dirname(path)
# path (str) – путь к файлу
# Возвращает строку, путь к родительской папки файла
# print(os.path.dirname("/home/janus/www/python-g22/files/main.py"))

# os.path.exists(path)
# Возвращает True|False, существует ли указанный путь в системе
# exist = os.path.exists(u'/home/janus/www/python-g22/files/')
# print(exist)

# os.path.isabs(path)
# path (str) – путь к файлу/папке
# Returns True или False
# проверяет путь на абсолютность
thisIs = os.path.isabs("/home/janus/www/python-g22/files/main.py")
print(thisIs)
# os.path.isdir(path)
# Возвращает True|False, является ли указанный путь катологом
thisIs = os.path.isdir(u'/home/janus/www/python-g22/files/')

print(thisIs)
# os.path.isfile(path)
# path (str) – путь к файлу или каталогу
# проверяет, указывает ли путь к файлу
thisIs = os.path.isfile("/home/janus/www/python-g22/files/main.py")

print(thisIs)
# os.path.islink(path)
# проверяет, указывает ли путь к символической ссылке
thisIs = os.path.islink(u'/home/janus/www/python-g22/files/')
print(thisIs)

# os.path.normpath(path)
# path (str) – путь к файлу/папке
# возвращает строку, нормализованный путь согласно операционной системы
# p = r'/home/janus/www/python-g22/files/'
# os.path.normpath(p)

# os.path.realpath(path)
# Возвращает путь к файлу символьной ссылки
# linux
# os.path.realpath("symlink_path") # "real_path"

# os.path.getatime(path)
# path – путь к файлу
# Raises: WindowsError – если файл не существует
# Возвращает время последнего доступа к файлу или папке, в виде количества секунд, прошедших с начала эпохи.

# os.path.getctime(path)
# path – путь к файлу
# Raises: WindowsError – если файл не существует
# Возвращает дату создания файла или папки, в виде количества секунд, прошедших с начала эпохи

# os.path.getmtime(path)
# path – путь к файлу
# Raises: WindowsError – если файл не существует
# Возвращает время последнего внесения изменения в файл или папку, в виде количества секунд, прошедших с начала эпохи

# os.path.expanduser(username)
# username - str, имя пользователя
# Возвращает путь к пользовательской папке
print(os.path.expanduser('~'))

# os.path.getsize(path)
# path – путь к файлу
# Raises: WindowsError – если файл не существует
# Возвращает размер файла или папки

# получить статистическую информацию о текущем каталоге:
# общий размер каталога в байтах, число файлов, число подкаталогов.

sums = [0,0,1] # 0 bytes, 0 files, 1 directory so far

def stat(path):
    tree = os.walk(path)
    for address, dirs, files in tree:
        for file in files:
            if os.path.isfile(file):
                sums[0] += os.path.getsize(file)
                sums[1] += 1
            else:
                sums[2] += 1
            print(address+'/'+file)
    return sums

# print(stat('./'))

# os.path.join(path1, path3, ...)
# Объединяет пути.
# р = os.path.join(r"C:\\", "book/folder/", "file.txt")

# Вывести рекурсивно список файлов и подкаталогов для данного каталога: 
def walk(dir):
 for name in os.listdir(dir):
   path = os.path.join(dir, name)
   if os.path.isfile(path):
       print(path)
   else:
       walk(path)

path = r'/home/janus/www/python-g22'
# walk(path)


# os.path.split(path)
# path (str) – путь к файлу
# Возвращает кортеж из пары строк - (путь к родителской папке, название файла).

# os.path.split('c:\\system\\apps\\Python\\Python.app')

# os.path.splitdrive(path)
# path (str) – путь к файлу
# Возвращает кортеж из пары строк - (имя диска, остальная часть пути).

# os.path.splitdrive ('c:\\system\\apps\\Python\\Python.app')

# os.path.splitext(path)
# path (str) – путь к файлу
# Возвращает кортеж из пары строк - (путь к файлу без расширения, расширение файла)
# os.path.splitext ('c:\\system\\apps\\Python\\Python.app')
