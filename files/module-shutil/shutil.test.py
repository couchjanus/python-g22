import shutil
import os
# shutil.test.py
# shutil.copy(source, destination) 
# копирует файл из source в destination.
# shutil.copy('C:\\file.txt', 'C:\\folder')  
# копируем file.txt в папку folder 
# если папки не существует, то file.txt копируется в файл с именем folder

# shutil.copy('file.txt', 'C:\\folder\\copyFile.txt')  
# копирование с переименовыванием
# Если файл с таким именем существует, то он будет заменен

# Скопировать дерево:
# shutil.copytree(source, destination) - скопирует папку со всем содержимым
# shutil.copytree('C:\\folder', 'C:\\folder_backup')  
# копируем папку (если папка с именем folder_backup существует, получим исключение (ошибку)) 

os.mkdir('../shutil-dir')
os.makedirs('../shutil-dir/one/tow/three')

shutil.copytree('../shutil-dir', '../copy-shutil-dir')
os.listdir('../copy-shutil-dir')

# Перемещение и переименовывание.
# shutil.move(source, destination) - перемещает файл или папку
# shutil.move('C:\\test.txt', 'C:\\folder')  
# Если папки folder не существует, файл переименуется в 'folder'. 
# Если в папке folder существует файл test.txt, то он перезапишется
# shutil.move('C:\\test.txt', 'C:\\folder\\new_test.txt')

# Пример переименовывания:
# shutil.move('C:\\test.txt', 'C:\\new_test.txt')

# Перемещение|переименование дерева:
shutil.move('../copy-shutil-dir', 'copy-shutil-dir')
os.listdir()

# Удаление дерева:
shutil.rmtree('../shutil-dir')
shutil.rmtree('copy-shutil-dir')
os.listdir()
