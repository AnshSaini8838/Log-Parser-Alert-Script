# 🔧 Log Parser & Alert Script with Python

A Python-based script that parses a log file of IP addresses and removes unauthorized ones while generating alert messages and maintaining a log of removed entries.

---

## 📌 Project Description

This project simulates the responsibilities of a SOC (Security Operations Center) Analyst by automating the task of managing IP allowlists. The script:

- Parses a file containing IP addresses (`allow_list.txt`).
- Removes IPs that are no longer authorized (`remove_list`).
- Generates alert messages when such IPs are found and removed.
- Logs each removal event in a separate log file (`removed_ips.log`).
- Validates the format of IPs before processing.

---

## 🎯 Objective

To demonstrate basic cybersecurity automation through:
- Log parsing
- Alert generation
- Access control via file manipulation
- Python scripting

---

## 🛠️ Technologies Used

- Python 3.x
- Text file I/O
- Regular Expressions (`re`)
- Date/Time module (`datetime`)

---

## ⚙️ How It Works

1. Loads the list of authorized IPs from `allow_list.txt`.
2. Defines a list of blacklisted IPs to be removed.
3. Validates IP format before removal.
4. Removes any matches from the main list.
5. Prints an alert for each removal.
6. Logs all removals to `removed_ips.log` with a timestamp.
7. Overwrites the original IP file with the updated list.
