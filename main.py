import socket

target = "127.0.0.1"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

result = sock.connect_ex((target, port))

if result == 0:
    print(f"{port} is OPEN")
else:
    print(f"{port} is CLOSED")

sock.close()