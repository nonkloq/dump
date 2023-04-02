import socket

host = 'localhost'
port = 4238

DNS_RECORDS = {
    'example.com': '192.168.1.100',
    'google.com': '172.217.167.78',
    'facebook.com': '69.63.176.13',
    'wikipedia.org': '98.12.123.34'
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print(f"DNS server listening on {host}:{port}")

try:
    while True:
        req, addr = sock.recvfrom(1024)
        req = req.decode()
        print(f"Request[{req}] from[{addr}]")
        response = DNS_RECORDS.get(req,"Domain not found")
        sock.sendto(response.encode(), addr)
except KeyboardInterrupt:
    print("\nDNS server closing...")
finally:
    sock.close()