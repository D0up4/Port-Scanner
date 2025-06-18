# 🔍 TCP Port Scanner (Python)

**Author:** D0up4 
**Project Type:** Red Team Recon / Educational  
**Last Updated:** 06/2025

---

## 📘 Description

This is a lightweight, terminal-based TCP port scanner written in Python. It scans a specified IP or hostname over a range of TCP ports and reports which ones are open. This tool is ideal for red team simulations, penetration testing labs, and cybersecurity training environments.

It performs simple TCP connect scans (like Nmap’s `-sT`), using raw sockets with adjustable timeouts and port ranges.

---

## ⚙️ Features

- ✅ Scans custom TCP port ranges (1–65535)
- ✅ Shows open and closed ports (optional)
- ✅ Minimal dependencies (pure Python)
- ✅ Timestamped output and scan duration
- ✅ Safe for educational and lab use

---

## 🚀 How To Use

- python port_scanner.py 127.0.0.1 --start 1 --end 65535

---

## 🛠️ Sample Output

🔍 Scanning 45.33.32.156 on ports 20–100...

🟢 Port 22 is OPEN
🟢 Port 80 is OPEN
🔴 Port 23 is CLOSED
🔴 Port 25 is CLOSED

✅ Scan complete in 0:00:01.752000
