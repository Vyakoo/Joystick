import socket
data = ''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.connect(('192.168.56.1', 3300))  # подключемся к серверному сокету

def x(x):
	global data
	sock.send(x.encode())  # отправляем сoобщение
	data = sock.recv(1024)  # читаем ответ от серверного сокета

x('12')
sock.close()  # закрываем соединение
print(data)