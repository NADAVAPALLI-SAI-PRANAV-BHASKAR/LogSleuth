from collections import Counter

with open("sample.log", "r") as file:
    logs = file.readlines()

ips = []
failed_ips = []

for line in logs:
    parts = line.strip().split()

    ip = parts[0]
    event = parts[1]

    ips.append(ip)

    if event == "LOGIN_FAILED":
        failed_ips.append(ip)

ip_count = Counter(ips)
failed_count = Counter(failed_ips)

print("===== LogSleuth Report =====\n")

print("Top IP Addresses:")
for ip, count in ip_count.most_common():
    print(f"{ip} - {count} requests")

print("\nPotential Brute Force Sources:")

for ip, count in failed_count.items():
    if count >= 5:
        print(ip)
