# 🔍 Port Scanner (Python)

A lightweight, multithreaded TCP port scanner built in Python for network reconnaissance and cybersecurity learning.  
This tool scans a target IP address, identifies open ports, maps them to common services, and exports results in structured JSON format.

---

## 📌 Features

- ⚡ Fast multithreaded scanning using `ThreadPoolExecutor`
- 🔌 TCP port scanning using Python sockets
- 🧠 Service name detection for common ports
- 📊 Structured scan results in JSON format
- ⏱ Scan duration tracking
- 🧾 Clean CLI interface using `argparse`
- 🧱 Modular project structure (production-style layout)

---

## 🏗 Project Structure

```
port-scanner/
│
├── scanner/
│   ├── scanner.py        # Core scanning logic
│   ├── ports.py          # Common port-service mappings
│   └── exporter.py       # JSON report generator
│
├── reports/
│   └── sample_report.json  # Example scan output
│
├── main.py               # CLI entry point
├── README.md
└── .gitignore
```

---

## 🚀 How It Works

The scanner attempts to establish a **TCP connection** to a list of ports on a target machine.

- If the connection succeeds → `OPEN`
- If the connection is refused → `CLOSED`
- If the connection times out → `FILTERED`

It uses Python’s `socket` library to perform low-level network communication.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```

Make sure Python 3 is installed:

```bash
python3 --version
```

No external dependencies are required.

---

## ▶️ Usage

### Scan default common ports

```bash
python3 main.py --target 127.0.0.1
```

### Scan specific ports

```bash
python3 main.py --target 127.0.0.1 --ports 22,80,443
```

---

## 📊 Example Output

```
Scanning target: 127.0.0.1

[OPEN] 22/tcp (SSH)
[CLOSED] 25/tcp (SMTP)
[FILTERED] 443/tcp (HTTPS)

Scan completed in 0.42 seconds
Results saved to reports/scan_results.json
```

---

## 📁 JSON Report Example

```json
{
    "target": "127.0.0.1",
    "results": [
        {
            "port": 22,
            "service": "SSH",
            "status": "OPEN"
        },
        {
            "port": 80,
            "service": "HTTP",
            "status": "CLOSED"
        },
        {
            "port": 443,
            "service": "HTTPS",
            "status": "FILTERED"
        }
    ]
}
```

---

## 🧠 Concepts Covered

- TCP/IP networking fundamentals
- Socket programming in Python
- Multithreading for performance optimization
- Command-line interface (CLI) design
- Data serialization using JSON
- Basic network reconnaissance techniques

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.  
Do not scan networks or systems you do not own or have explicit permission to test.

---

## 📈 Future Improvements

- UDP scanning support
- Banner grabbing (service version detection)
- CSV/HTML report export
- Colored terminal output
- Scan progress indicator
- Async IO version for higher performance

---

## 👨‍💻 Author

Built as a cybersecurity learning project to understand:
- network scanning
- socket programming
- and basic reconnaissance techniques

---

⭐ If you like this project, consider starring the repository!
```