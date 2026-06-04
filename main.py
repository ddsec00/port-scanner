import socket
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <target_ip>")
    sys.exit(1)

target = sys.argv[1]

ports = [22, 80, 443, 21, 25]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"{port}/tcp OPEN")
    else:
        print(f"{port}/tcp CLOSED")

    sock.close()