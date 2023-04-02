import socket

HOST = 'localhost'
PORT = 6900
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"Listening on {HOST}:{PORT}...")

conn, addr = sock.accept()
print(f"Connected by {addr}...")

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    data = data.decode()

    print("Recieved Message:",data)
    data += " 🙂\n"
    conn.sendall(data.encode())

conn.close()
sock.close()
print("\nServer Closed")