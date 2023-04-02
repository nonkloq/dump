import socket

server_address = ('localhost', 5678)
socket_handle = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Select a protocol: ")
print("1. ARP")
print("2. RARP")
protocol = int(input("Enter your Protocol: "))
if 1<protocol>2:
    print("Invalid choice.")
    exit()

if protocol == 1:
    opcode = "ARP_REQUEST"
    target_ip = input("Enter target IP address: ")
    message = f"{opcode},,192.168.1.100,ff:ff:ff:ff:ff:ff,{target_ip}"
elif protocol == 2:
    opcode = "RARP_REQUEST"
    target_mac = input("Enter target MAC address: ")
    message = f"{opcode},,192.168.1.100,{target_mac},0.0.0.0"
    
socket_handle.sendto(message.encode(), server_address)
print(f"Sent {opcode} to {server_address}")

response, _ = socket_handle.recvfrom(1024)
print(f"Received response: {response.decode()}")
