import socket
import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="123456",
  host="127.0.0.1",
  port="5434"
)
sock = socket.socket()
sock.bind(('', 9091))
while True:
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected', addr)
    data = conn.recv(1024)
    if not data:
        break
    string = data.decode('utf-8')

#поиск информации
    cur = con.cursor()
    cur.execute("SELECT name, password from LOGIN")
    rows = cur.fetchall()
    for row in rows:
        name = row[0] + row[1]
        if (string == name):
            res = 'Name = ' + row[0] + ' pass = ' + row[1]
            break
        else:
            res = 0
    if (res == 0):
        conn.send('Такого пользователя нет'.encode('utf-8'))
    else:
        conn.send(res.encode('utf-8'))

conn.close()