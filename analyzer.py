from collections import Counter
from datetime import datetime
import os

print("=" * 50)
print("LogSleuth - Log Analysis & Threat Detection Tool")
print("=" * 50)

try:
    log_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "sample.log"
    )

    with open(log_path, "r") as file:
        logs = file.readlines()

except FileNotFoundError:
    print("sample.log not found")
    input("\nPress Enter to exit...")
    exit()

ips = []
failed_ips = []

for line in logs:
    parts = line.strip().split()

    if len(parts) != 2:
        continue

    ip = parts[0]
    event = parts[1]

    ips.append(ip)

    if event == "LOGIN_FAILED":
        failed_ips.append(ip)

ip_count = Counter(ips)
failed_count = Counter(failed_ips)

print("\n===== LogSleuth Analysis Report =====\n")

print("Top IP Addresses:")
for ip, count in ip_count.most_common():
    print(f"{ip} - {count} requests")

print(f"\nTotal Failed Login Attempts: {len(failed_ips)}")

print("\nSuspicious IP Addresses (3-4 failed logins):")

found = False

for ip, count in failed_count.items():
    if 3<=count< 5:
        print(f"{ip} ({count} failed logins)")
        found = True

if not found:
    print("None")

print("\nPotential Brute Force Sources (5 or more failed logins):")

found = False

for ip, count in failed_count.items():
    if count >= 5:
        print(f"{ip} ({count} failed logins)")
        found = True

if not found:
    print("None")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"report_{timestamp}.txt"

report_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    filename
)

with open(report_path, "w") as report:
    report.write("LogSleuth Analysis Report\n")
    report.write("=" * 40 + "\n")

    report.write(
        f"Total Log Entries: {len(logs)}\n"
    )

    report.write(
        f"Total Failed Login Attempts: "
        f"{len(failed_ips)}\n\n"
    )

    report.write("Top IP Addresses:\n")

    for ip, count in ip_count.most_common():
        report.write(
            f"{ip} - {count} requests\n"
        )

    report.write("\n")

    report.write(
        "Suspicious IP Addresses (3-4 failed logins):\n"
    )

    found = False

    for ip, count in failed_count.items():
        if 3<=count<5:
            report.write(
                f"{ip} ({count} failed logins)\n"
            )
            found = True

    if not found:
        report.write("None\n")

    report.write("\n")

    report.write(
        "Potential Brute Force Sources (5 or more failed logins):\n"
    )

    found = False

    for ip, count in failed_count.items():
        if count >= 5:
            report.write(
                f"{ip} ({count} failed logins)\n"
            )
            found = True

    if not found:
        report.write("None\n")

print(f"\nReport saved as {filename}")

input("\nPress Enter to exit...")
