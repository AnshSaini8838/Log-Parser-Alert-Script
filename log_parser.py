# Log Parser & Alert Script with Python

# File name containing the allowed IPs
import_file = "allow_list.txt"

# List of IPs to remove
remove_list = [
    "192.168.97.225",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

# Step 1: Read the file contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Step 2: Convert the content to a list
ip_addresses = ip_addresses.split()

# Step 3: Remove IPs from the list that are in remove_list
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Step 4: Convert list back to string with each IP on a new line
ip_addresses = "\n".join(ip_addresses)

# Step 5: Overwrite the original file with updated IPs
with open(import_file, "w") as file:
    file.write(ip_addresses)

print("Updated IP list saved successfully.")
