import socket

host = 'info.cern.ch' # not secured  http website
port = 80 # http port number

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))

request = "GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n"
sock.send(request.encode())

response = ""
while True:
    data = sock.recv(1024)
    if not data: break
    response += data.decode()

print(response)

sock.close()
