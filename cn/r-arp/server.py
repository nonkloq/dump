import socket

arp_table = {
    "192.168.1.101": "00:11:22:33:44:55",
    "192.168.1.102": "11:22:33:44:55:66",
    "192.168.1.103": "22:33:44:55:66:77"
}

rarp_table = {
    "00:11:22:33:44:55": "192.168.1.101",
    "11:22:33:44:55:66": "192.168.1.102",
    "22:33:44:55:66:77": "192.168.1.103"
}

socket_handle = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_handle.bind(('0.0.0.0', 5678))

try:
    while True:
        message, client_address = socket_handle.recvfrom(1024)
        print(f"Received message: {message} from {client_address}")

        opcode, sender_mac, sender_ip, target_mac, target_ip = message.decode().split(",")
        print(f"opcode={opcode}, sender_mac={sender_mac}, sender_ip={sender_ip}, target_mac={target_mac}, target_ip={target_ip}")

        if opcode == "ARP_REQUEST":
            if target_ip in arp_table:
                arp_reply = f"ARP_REPLY,{arp_table[target_ip]},{target_ip},{sender_mac},{sender_ip}"
                socket_handle.sendto(arp_reply.encode(), client_address)
                print(f"Sent ARP_REPLY to {client_address}")
            else: print(f"No ARP entry found for {target_ip}")

        elif opcode == "RARP_REQUEST":
            if target_mac in rarp_table:
                rarp_reply = f"RARP_REPLY,{target_mac},{rarp_table[target_mac]}"
                socket_handle.sendto(rarp_reply.encode(), client_address)
                print(f"Sent RARP_REPLY to {client_address}")
            else: print(f"No RARP entry found for {target_mac}")
except KeyboardInterrupt: print("\nServer Closed!")
finally: socket_handle.close()