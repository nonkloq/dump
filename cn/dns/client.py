import socket

host = 'localhost'
port = 4238
addr = (host,port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(addr)

while True:
    req = input("Domain Name(exit): ")
    if req == "exit": break
    sock.sendto(req.encode(),addr)
    resp,addr = sock.recvfrom(1024)
    print(f"> {req}: {resp.decode()}")


sock.close()