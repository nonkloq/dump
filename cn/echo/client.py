import socket

HOST = 'localhost'
PORT = 6900
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    message = input("Message to echo server: ")
    if message == "exit": 
        print("\nClient Exiting...")
        break
    sock.sendall(message.encode())
    data = sock.recv(BUFFER_SIZE)
    print(f"Received Message: {data.decode()}")

sock.close()
