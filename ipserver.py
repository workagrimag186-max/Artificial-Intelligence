import socket
import ipaddress

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("========================================")
print("       IP ADDRESSING SERVER")
print("========================================")
print("Port :", PORT)
print("Waiting for client...")

client, address = server.accept()

print("Client connected :", address)

while True:

    menu = """
========================================
        IP ADDRESSING SERVER
========================================
1. Analyze IPv4 Address
2. Subnet Analysis
3. Check Same Network
4. IP Address to Binary
5. Client IP Information
6. Exit
========================================
Enter your choice:
"""

    client.send(menu.encode())

    choice = client.recv(1024).decode()

    # OPTION 1
    if choice == "1":

        client.send(b"Enter IPv4 address: ")
        ip = client.recv(1024).decode()

        address_ip = ipaddress.IPv4Address(ip)

        first = int(ip.split(".")[0])

        if first <= 126:
            ip_class = "Class A"
            mask = "255.0.0.0"
        elif first <= 191:
            ip_class = "Class B"
            mask = "255.255.0.0"
        elif first <= 223:
            ip_class = "Class C"
            mask = "255.255.255.0"
        elif first <= 239:
            ip_class = "Class D"
            mask = "N/A"
        else:
            ip_class = "Class E"
            mask = "N/A"

        binary = format(int(address_ip), "032b")

        binary = binary[0:8] + "." + binary[8:16] + "." + binary[16:24] + "." + binary[24:32]

        result = f"""
========================================
           IPv4 ANALYSIS
========================================
IP Address      : {address_ip}
IP Class        : {ip_class}
Default Mask    : {mask}
Private Address : {address_ip.is_private}
Loopback        : {address_ip.is_loopback}
Multicast       : {address_ip.is_multicast}
Global Address  : {address_ip.is_global}
Reserved        : {address_ip.is_reserved}
Binary Address  : {binary}
========================================
"""

        client.send(result.encode())

    # OPTION 2
    elif choice == "2":

        client.send(b"Enter IPv4 address: ")
        ip = client.recv(1024).decode()

        client.send(b"Enter CIDR prefix: ")
        prefix = int(client.recv(1024).decode())

        network = ipaddress.ip_network(ip + "/" + str(prefix), strict=False)

        total = network.num_addresses

        if total >= 2:
            usable = total - 2
        else:
            usable = 0

        hosts = list(network.hosts())

        if len(hosts) > 0:
            first_host = hosts[0]
            last_host = hosts[-1]
        else:
            first_host = "N/A"
            last_host = "N/A"

        result = f"""
========================================
           SUBNET ANALYSIS
========================================
IP Address     : {ip}
CIDR Prefix    : /{prefix}
Subnet Mask    : {network.netmask}
Network        : {network.network_address}
Broadcast      : {network.broadcast_address}
First Host     : {first_host}
Last Host      : {last_host}
Total Addresses: {total}
Usable Hosts   : {usable}
========================================
"""

        client.send(result.encode())

    # OPTION 3
    elif choice == "3":

        client.send(b"Enter first IPv4 address: ")
        ip1 = client.recv(1024).decode()

        client.send(b"Enter second IPv4 address: ")
        ip2 = client.recv(1024).decode()

        client.send(b"Enter CIDR prefix: ")
        prefix = int(client.recv(1024).decode())

        network1 = ipaddress.ip_network(ip1 + "/" + str(prefix), strict=False)
        network2 = ipaddress.ip_network(ip2 + "/" + str(prefix), strict=False)
        if network1.network_address == network2.network_address:
            result = f"""
========================================
         NETWORK COMPARISON
========================================
IP 1    : {ip1}
IP 2    : {ip2}
Prefix  : /{prefix}

Result  : SAME NETWORK
Network : {network1.network_address}/{prefix}
========================================
"""
        else:
            result = f"""
========================================
         NETWORK COMPARISON
========================================
IP 1      : {ip1}
IP 2      : {ip2}
Prefix    : /{prefix}

Result    : DIFFERENT NETWORKS
Network 1 : {network1.network_address}/{prefix}
Network 2 : {network2.network_address}/{prefix}
========================================
"""
        client.send(result.encode())
    elif choice == "4":

        client.send(b"Enter IPv4 address: ")
        ip = client.recv(1024).decode()

        address_ip = ipaddress.IPv4Address(ip)

        binary = format(int(address_ip), "032b")

        binary = binary[0:8] + "." + binary[8:16] + "." + binary[16:24] + "." + binary[24:32]

        result = f"""
========================================
          IP TO BINARY
========================================
IP Address : {ip}
Binary     : {binary}
========================================
"""
        client.send(result.encode())
    elif choice == "5":
        result = f"""
========================================
        CLIENT INFORMATION
========================================
Client IP   : {address[0]}
Client Port : {address[1]}
========================================
"""
        client.send(result.encode())
    elif choice == "6":
        client.send(b"Connection closed. Thank you!\n")
        break
client.close()
server.close()