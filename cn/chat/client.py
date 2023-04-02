import socket
import threading

HOST = 'localhost'
PORT = 4200
BUFFER_SIZE = 1024
name = input("your name: ")



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def receive_messages():
    while True:
        data = sock.recv(BUFFER_SIZE)
        if not data:break
        print(data.decode())

    print("Connection closed by server [Enter to exit].")
    return 


print("\tYou joined the unwanted Group")
sock.sendall(("\t"+name+"joined the group!").encode())


receive_thread = threading.Thread(target=receive_messages,daemon=True)
receive_thread.start()

is_in = True
while is_in:
    message = input("")
    if not receive_thread.is_alive(): break

    if message == "bye": 
        is_in = False
        message = "\t"+name+" left the chat."
    else: message= f"{name}: " + message
    sock.sendall(message.encode())

sock.close()