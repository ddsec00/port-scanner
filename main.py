import argparse
import time

from concurrent.futures import ThreadPoolExecutor

from scanner.scanner import scan_port
from scanner.scanner import parse_ports
from scanner.exporter import save_json_report


def main():

    parser = argparse.ArgumentParser(
        description="Simple TCP Port Scanner"
    )

    parser.add_argument(
        "--target",
        required=True,
        help="Target IP address"
    )

    parser.add_argument(
        "--ports",
        help="Comma-separated ports"
    )

    args = parser.parse_args()

    target = args.target

    ports = parse_ports(args.ports)

    print(f"\nScanning target: {target}\n")

    start_time = time.time()

    results = []

    with ThreadPoolExecutor(max_workers=20) as executor:

        futures = []

        for port, service in ports.items():

            future = executor.submit(
                scan_port,
                target,
                port,
                service
            )

            futures.append(future)

        for future in futures:
            results.append(
                future.result()
            )

    end_time = time.time()

    duration = end_time - start_time

    save_json_report(
        target,
        results
    )

    print(
        f"\nScan completed in "
        f"{duration:.2f} seconds"
    )

    print(
        "Results saved to "
        "reports/scan_results.json"
    )


if __name__ == "__main__":
    main()