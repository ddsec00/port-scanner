import socket

from scanner.ports import COMMON_PORTS


def scan_port(target, port, service):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)

    try:
        sock.connect((target, port))

        status = "OPEN"

    except socket.timeout:
        status = "FILTERED"

    except ConnectionRefusedError:
        status = "CLOSED"

    except OSError:
        status = "FILTERED"

    finally:
        sock.close()

    print(f"[{status}] {port}/tcp ({service})")

    return {
        "port": port,
        "service": service,
        "status": status
    }


def parse_ports(port_string):
    if not port_string:
        return COMMON_PORTS

    ports = {}

    for p in port_string.split(","):
        try:
            port = int(p.strip())

            ports[port] = COMMON_PORTS.get(
                port,
                "UNKNOWN"
            )

        except ValueError:
            continue

    return ports