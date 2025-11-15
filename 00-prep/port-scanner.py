#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

def scan_target(target, ports):
    print(f"[*] Scanning {target} - {datetime.now()}\n")
    open_ports = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] Port {port}/tcp OPEN")
            open_ports.append(port)
        sock.close()
    
    return open_ports

# --- CONFIG ---
target = "scanme.nmap.org"  # ALLOWED FOR TESTING
ports = [22, 80, 443, 8080, 21, 25, 53]
# ----------------

if __name__ == "__main__":
    open_ports = scan_target(target, ports)
    if open_ports:
        print(f"\n[!] Open ports: {open_ports}")
    else:
        print("\n[-] No open ports found.")