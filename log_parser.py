import re
from datetime import datetime

# File name containing the allowed IPs
import_file = "allow_list.txt"

# File to log removed IPs
log_file = "removed_ips.log"

# List of IPs to remove
remove_list = [
    "192.168.97.225",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

# Function to validate IPv4 format
def is_valid_ip(ip):
    pattern = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
    return pattern.match(ip) is not None

# Step 1: Read the file contents
with open(import_file, "r") as file:
    ip_addresses = file.read().split()

# Step 2: Open log file for appending
with open(log_file, "a") as log:
    for ip in remove_list:
        if not is_valid_ip(ip):
            print(f"[WARNING] Skipped invalid IP format: {ip}")
            continue

        if ip in ip_addresses:
            ip_addresses.remove(ip)
            print(f"[ALERT] Blacklisted IP removed: {ip}")

            # Log the removal with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"{timestamp} - Removed IP: {ip}\n")

# Step 3: Write updated IP list back to the file
with open(import_file, "w") as file:
    file.write("\n".join(ip_addresses))

print("✅ IP list updated and alerts logged.")
