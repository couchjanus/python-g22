# 01_sqlight.py
# Подключаем модуль sqlite3
import sqlite3

print(sqlite3.threadsafety)
print(sqlite3.paramstyle)

print(sqlite3.version)
# '2.6.0' - это версия pysqlite

# Получаем номер спецификации

# Получить номер версии используемого модуля sqliteЗ
# можно с помощью атрибутов sqlite_version и sqlite_version_info.

# Атрибут sqlite_version возвращает номер версии в виде строки
print(sqlite3.sqlite_version)

# Атрибут sqlite_version_info - в виде кортежа из трех или четырех чисел.
print(sqlite3.sqlite_version_info)


# Открываем базу данных
print('Открываем базу данных')
con = sqlite3.connect("testdb.db")

# Работаем с базой данных
if con:
    print('Работаем с базой данных')
# Закрьmаем базу данных
print('Закрьmаем базу данных')
con.close()

# Доступ к базе, хранящейся: в файле c:\book\testdb.db

# con = sqlite3.connect(r"file:///c:/book/testdb.db", uri = True)
con = sqlite3.connect(r"file:////home/janus/www/python-base/sql/testdb.db?mode=rwc", uri = True)
# Закрьmаем базу данных
con.close()

# Доступ только для чтения
# con = sqlite3.connect(r"file:///c:/book/testdb.db?mode = ro", uri =True)
con = sqlite3.connect(r"file:////home/janus/www/python-base/sql/testdb.db?mode=ro", uri = True)
# Закрьmаем базу данных
con.close()

# Доступ к неизменяемой базе данных
# con = sqlite3.connect(r"file:///f:/testdb.db?immutable=1", uri = True)
con = sqlite3.connect(r"file:////home/janus/www/python-base/sql/testdb.db?immutable=1", uri = True)
con.close()
