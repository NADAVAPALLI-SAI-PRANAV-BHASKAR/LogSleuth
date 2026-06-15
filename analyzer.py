from collections import Counter

print("=" * 50)
print("LogSleuth - Log Analysis & Threat Detection Tool")
print("=" * 50)

try:
    with open("sample.log", "r") as file:
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

print("\n===== LogSleuth Report =====\n")

print("Top IP Addresses:")
for ip, count in ip_count.most_common():
    print(f"{ip} - {count} requests")

print(f"\nTotal Failed Login Attempts: {len(failed_ips)}")

print("\nPotential Brute Force Sources:")

found = False

for ip, count in failed_count.items():
    if count >= 5:
        print(ip)
        found = True

if not found:
    print("None")

with open("report.txt", "w") as report:
    report.write("===== LogSleuth Report =====\n\n")

    report.write("Top IP Addresses:\n")
    for ip, count in ip_count.most_common():
        report.write(f"{ip} - {count} requests\n")

    report.write(
        f"\nTotal Failed Login Attempts: {len(failed_ips)}\n"
    )

    report.write("\nPotential Brute Force Sources:\n")

    found = False

    for ip, count in failed_count.items():
        if count >= 5:
            report.write(f"{ip}\n")
            found = True

    if not found:
        report.write("None\n")

print("\nReport saved as report.txt")

input("\nPress Enter to exit...")
