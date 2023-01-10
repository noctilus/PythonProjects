#! /usr/bin/env python3

"""Nmap scanner automation.
inspired by HackerSploit @ YouTube"""

import ipaddress
import nmap


print("\nNetwork scanner with nmap")
print("-"*30, "\n")

ip_addr = input("Enter IP address to scan: ")

print("Target set to: ", ip_addr)

try:
    # validate if IP given is correct
    ip_address = ipaddress.ip_address(ip_addr)
    print("IP", ip_address, "seems valid")
except ValueError as errormsg:
    z = ValueError()
    print("\n", errormsg, "\n")
    print("I give up ...")
    # print(ValueError)
    # print(ValueError)
    quit()


scanner_instance = nmap.PortScanner()


type(ip_address)

scan_type = input("""
\n Please define the type of scan:
    1) SYN ACK Scan
    2) UDP Scan
    3) Comprehensive Scan \n
""")
print("Scan type set to: ", scan_type)

if scan_type == '1':
    print("Nmap version: ", scanner_instance.nmap_version())
    scanner_instance.scan(ip_addr, "1-1024", "-v -sS")
    print(scanner_instance.scaninfo())
    print("IP status: ", scanner_instance[ip_addr].state())
    print(scanner_instance[ip_addr].all_protocols())
    print("Open ports: ", scanner_instance[ip_addr]["tcp"].keys())


if scan_type == '2':
    print("Nmap version: ", scanner_instance.nmap_version)
    scanner_instance.scan(ip_addr, "1-1024", "-v -sU")
    print(scanner_instance.scaninfo())
    print("IP status: ", scanner_instance[ip_addr].state())
    print(scanner_instance[ip_addr].all_protocols())
    print("Open ports: ", scanner_instance[ip_addr]["udp"].keys())

if scan_type == '3':
    print("Nmap version: ", scanner_instance.nmap_version)
    scanner_instance.scan(ip_addr, "1-1024", "-v -sS -sV -sC -A -O")
    print(scanner_instance.scaninfo())
    print("IP status: ", scanner_instance[ip_addr].state())
    print(scanner_instance[ip_addr].all_protocols())
    print("Open ports: ", scanner_instance[ip_addr]["tcp"].keys())
