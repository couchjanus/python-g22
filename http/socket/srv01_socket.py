# Сервер TCP srv01_socket.py

# Суть TCP-соединения: 
# одна программа устанавливает соединение с другой, 
# и они обмениваются данными, причём их потери не происходит. 
# После завершения работы соединение должно быть закрыто.

# Для работы с сокетами нужно импортировать модуль socket:
import socket

# Код модуля socket является объектно-ориентированной-оберткой 
# вокрут набора системных вызовов для работе с сокетами. 

# Его можно представить себе, как:

# class socket:  # имя класса с маленькой буквы
#     def __init__(domain, type, proto):
#         self._fd = system_socket(domain, type, proto)

#     def write(data):
#         # вместо write используется send
#         system_write(self._fd, data)

#     def fileno():
#         return self._fd


# API-вызовы, которые сервер делает для настройки слушающего сокета:
# socket()
# bind()
# listen()
# accept()


# для инициализации сокета введен одноименный системный вызов socket(). 

# создать сокет:
# server_sock = socket.socket()
# print(type(server_sock))           # <class 'socket.socket'>


# Определим тип сокета как socket.SOCK_STREAM. 
# По умолчанию используется протокол управления передачей (TCP).

# socket.socket() создает объект сокета

print('AddressFamily: ', socket.AF_INET)  # AddressFamily.AF_INET
print('SocketKind: ', socket.SOCK_STREAM)  # SocketKind.SOCK_STREAM

# Аргументы, передаваемые функции socket(), определяют семейство адресов и тип сокета. 
# AF_INET - это семейство интернет-адресов для IPv4. 
# SOCK_STREAM - это тип сокета для TCP, протокола, который будет использоваться для передачи сообщений.

server_sock = socket.socket(
    socket.AF_INET,      # задамем семейство протоколов 'Интернет' (INET)
    socket.SOCK_STREAM,  # задаем тип передачи данных 'потоковый' (TCP)
    proto=0)             # выбираем протокол 'по умолчанию' для TCP, т.е. IP

# доступ к целочисленному файловому дескриптору можно получить с помощью:
print('доступ к целочисленному файловому дескриптору:')
print('server_sock.fileno()= ', server_sock.fileno())  # int
print('server_sock.proto= ', server_sock.proto)  # 0

# Для создания сервера нужно связать сокет с одним или всеми из имеющихся у компьютера 
# хостов (IP-адресов) и каким-либо свободным портом. 

# bind() используется для связи сокета с определенным сетевым интерфейсом и номером порта:

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# на серверной машине может быть несколько сетевых адаптеров, 
# нам необходимо привязать созданный сокет к одному из них:

server_sock.bind(('127.0.0.1', 53000))  

# чтобы привязать сразу ко всем, можно использовать ''

# Если не указать хост или указать "0.0.0.0", сокет будет прослушивать все хосты. 
# Если указать "127.0.0.1", то подключиться можно будет только с этого же компьютера.

server_sock.bind((HOST, PORT))

# Вызов bind() заставляет нас указать не только IP адрес, 
# но и порт, на котором сервер будет ожидать (слушать) подключения клиентов.
# функция bind принимает массив, содержащий два элемента: хост и порт.

# взаимодействие по сети происходит с помощью отправки пакетов, 
# а TCP требует установления соединения, 
# т.е. обмена между клиентом и сервером несколькими служебными пакетами, 
# не содержащими реальных бизнес-данных. 

# Каждое TCP соединение обладает состоянием. 
# их можно представить себе так:
# СОЕДИНЕНИЕ УСТАНАВЛИВАЕТСЯ -> УСТАНОВЛЕНО -> СОЕДИНЕНИЕ ЗАКРЫВАЕТСЯ

# необходимо явно перевести сокет в состояние ожидания подключения, 
# сообщив об этом операционной системе:

# функция listen принимает в качестве аргумента максимальное число соединений, 
# которые будут находиться в очереди соединений до вызова функции accept; 
# она не ограничивает максимальное число активных соединений в целом.

server_sock.listen()

# Когда клиент подключается, сервер вызывает accept(), чтобы принять или завершить соединение.

# После этого вызова операционная система готова принимать подключения от клиентов на этом сокете

server_sock.close()

# Параметр backlog
# server_sock.listen(10)  # 10 - это размер очереди входящих подключений (backlog)
# Параметр backlog определяет размер очереди для установленных соединений. 
# Пока количество подключенных клиентов меньше, чем этот параметр, 
# операционная система будет автоматически принимать входящие соединения на серверный сокет 
# и помещать их в очередь. 
# Как только количество установленных соединений в очереди достигнет значения backlog, 
# новые соединения приниматься не будут. 
# В зависимости от реализации, OC может явно отклонять новые подключения 
# или просто их игнорировать, давая возможность им дождаться освобождения места в очереди.
