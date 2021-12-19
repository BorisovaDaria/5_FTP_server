from pathlib import *
import socket
import os
'''
pwd - показывает название рабочей директории
ls - показывает содержимое текущей директории
cat <filename> - отправляет содержимое файла
'''

dirname = os.path.join(os.getcwd(), 'docs')

def process(req):
    if req == 'pwd':
        return dirname
    elif req == 'ls':
        return '; '.join(os.listdir(dirname))
    elif len(req.split()) == 2:
        if req.split()[0] == 'mf':
            Path.touch(Path.cwd() / 'docs' / req.split()[1])
            return 'file created successful'
        elif req.split()[0] == 'df':
            Path.unlink(Path.cwd() / 'docs' / req.split()[1])
            return 'file deleted successful'
        elif req.split()[0] == 'md':
            Path.mkdir(Path.cwd() / 'docs' / req.split()[1])
            return 'directory created successful'
        elif req.split()[0] == 'dd':
            Path.rmdir(Path.cwd() / 'docs' / req.split()[1])
            return 'directory deleted successful'
        elif req.split()[0] == 'cf':
            return Path.read_text(Path.cwd() / 'docs' / req.split()[1])
    elif len(req.split()) == 3:
        if req.split()[0] == 'rf':
            Path.rename(Path.cwd() / 'docs' / req.split()[1], Path.cwd() / 'docs' / req.split()[2])
            return 'file renamed successfully'
        elif req.split()[0] == 'pf':
            Path.write_text(Path.cwd() / 'docs' / req.split()[1], req.split()[2])
            return 'file pasted successfully'
    return 'bad request'


PORT = 6666

sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
print("Прослушиваем порт", PORT)

while True:
    conn, addr = sock.accept()
    
    request = conn.recv(1024).decode()
    print(request)
    if request == 'q':
        break
    response = process(request)
    conn.send(response.encode())

conn.close()
