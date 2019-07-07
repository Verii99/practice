import socket

sock = socket.socket()
sock.connect(('localhost', 9091))
a = input('Введите login: ')
b = input('Введите password: ')
string = a+" "+b
sock.send(string.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print(data.decode('utf-8'))