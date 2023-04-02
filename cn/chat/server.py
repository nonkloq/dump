import socket
import threading

HOST = 'localhost'
PORT = 4200
BUFFER_SIZE = 1024
clients = []


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"Server started and listening on {HOST}:{PORT}...")

def handle_client(conn, addr):
    clients.append(conn)
    print(f"Connected by {addr}...")
    
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        for client in clients:
            if client != conn: client.sendall(data)

    clients.remove(conn)
    print(f"Client {addr} disconnected.")
    conn.close()

try:
    while True:
        conn, addr = sock.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr),daemon=True)
        client_thread.start()
        
except KeyboardInterrupt:
    print("\nClossing The server!!")

finally:
    for conn in clients: conn.close()
    sock.close()
    print(f"Server and [{len(conn)}]Connections are closed!")