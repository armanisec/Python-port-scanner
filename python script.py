import socket

target = input("Enter the target IP address or website: ")

# List of ports you want to scan
ports = [22, 80, 443]

for port in ports:
    try:
        # Create a socket object
        s = socket.socket()
        s.settimeout(1)
        
        # Try to connect
        s.connect((target, port))
        print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        print(f"[-] Port {port} is CLOSED")
