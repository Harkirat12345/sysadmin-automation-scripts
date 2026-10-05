# TCP Port Scanner

A simple Python TCP port scanner that checks a specified range of ports on a target host.

## Features

- Accepts an IP address or domain name
- Allows the user to specify a starting and ending port
- Attempts TCP connections to each port
- Identifies open and closed ports
- Uses socket timeouts to prevent connections from hanging

## Usage

```bash
python portscanner.py
```

Example:

```text
Enter target IP or domain: 192.168.1.10
What is the starting port: 20
What is the ending port: 100
```

The program scans each port in the specified range and reports its status.

## How It Works

The script uses Python's `socket` library to create TCP connections.

For each port in the selected range, the program attempts a connection using `connect_ex()`.

A successful connection indicates that the port is open.

## Skills Demonstrated

- Python
- TCP/IP networking
- Socket programming
- Port scanning
- Network troubleshooting
- Loops and user input
- Basic network reconnaissance

## Disclaimer

This script is intended for educational, troubleshooting, and authorized network administration purposes. Only scan systems that you own or have permission to test.
