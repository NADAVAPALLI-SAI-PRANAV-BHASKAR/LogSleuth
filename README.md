# LogSleuth - Log Analysis & Threat Detection Tool

LogSleuth is a Python-based security log analysis tool that detects suspicious login activity and potential brute-force attacks from log files.

The project demonstrates log parsing, threat detection, data analysis, file handling, and basic cybersecurity monitoring techniques.

---

## Features

- Log file parsing
- IP activity analysis
- Failed login detection
- Suspicious IP identification
- Brute-force attack detection
- Timestamped report generation
- Input validation
- Automatic report storage

---

## Technologies Used

- Python
- Log Analysis
- Threat Detection
- File Handling
- Data Processing

---

## Requirements

- Python 3.10.0 or higher

No external dependencies are required.

---

## Project Structure

```text
LogSleuth/
│
├── analyzer.py
├── sample.log
├── README.md
├── requirements.txt
└── report_YYYYMMDD_HHMMSS.txt
```

---

## How It Works

1. Reads a log file.
2. Extracts IP addresses and login events.
3. Counts IP activity.
4. Detects failed login attempts.
5. Identifies suspicious IP addresses.
6. Detects potential brute-force attacks.
7. Generates a timestamped analysis report.

---

## Usage

Run the script:

```bash
py analyzer.py
```

or

```bash
python analyzer.py
```

---

## Sample Log

```text
192.168.1.10 LOGIN_FAILED
192.168.1.10 LOGIN_FAILED
192.168.1.10 LOGIN_FAILED
192.168.1.10 LOGIN_FAILED
192.168.1.10 LOGIN_FAILED
10.0.0.5 LOGIN_SUCCESS
10.0.0.5 LOGIN_SUCCESS
172.16.0.8 LOGIN_FAILED
172.16.0.8 LOGIN_SUCCESS
172.16.0.8 LOGIN_FAILED
192.168.1.15 LOGIN_SUCCESS
192.168.1.15 LOGIN_SUCCESS
192.168.1.15 LOGIN_SUCCESS
```

---

## Example Output

```text
===== LogSleuth Analysis Report =====

Top IP Addresses:
192.168.1.10 - 5 requests
172.16.0.8 - 3 requests
192.168.1.15 - 3 requests
10.0.0.5 - 2 requests

Total Failed Login Attempts: 7

Suspicious IP Addresses (3-4 failed logins):
None

Potential Brute Force Sources (5 or more failed logins):
192.168.1.10 (5 failed logins)
```

---

## Sample Report

```text
LogSleuth Analysis Report
========================================
Total Log Entries: 13
Total Failed Login Attempts: 7

Top IP Addresses:
192.168.1.10 - 5 requests
172.16.0.8 - 3 requests
192.168.1.15 - 3 requests
10.0.0.5 - 2 requests

Suspicious IP Addresses (3-4 failed logins):
None

Potential Brute Force Sources (5 or more failed logins):
192.168.1.10 (5 failed logins)
```

---

## Skills Demonstrated

- Security Log Analysis
- Threat Detection
- Brute Force Detection
- Data Processing
- File Handling
- Python Development

---

## Future Improvements

- Support for larger log formats
- Real-time log monitoring
- CSV and JSON report export
- Threat severity scoring
- Dashboard visualization

---

## Disclaimer

This project is intended for educational purposes and authorized security analysis only.

---

Thank you
