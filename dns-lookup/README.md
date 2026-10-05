# DNS Lookup Tool

A Python command-line tool for querying common DNS records for a domain.

## Features

The script retrieves:

- A records
- MX records
- TXT records
- CNAME records

The program prompts the user for a domain and validates that the domain can be resolved before displaying its DNS information.

## Requirements

- Python 3
- `dnspython`

Install the required package:

```bash
pip install dnspython
```

## Usage

```bash
python dns_lookup.py
```

Enter a domain when prompted:

```text
What is the domain that you want to look up? example.com
```

The script will display available DNS records associated with the domain.

## Skills Demonstrated

- Python
- DNS
- Network troubleshooting
- Exception handling
- Python libraries
- Command-line tools

## Purpose

This tool was created to practice DNS resolution and Python-based network troubleshooting commonly used in system administration and networking.
