# import sys
import datetime
import os
import platform

print("""
      1. Enter an IP range 
      2. first number to ping
      3. last number to ping

      Example:
      -192.168.0
      -2
      -8

      """)

user_input = input("Enter network IP: ")
ip_parts = user_input.split(".")
network_ip = ip_parts[0]+'.'+ip_parts[1]+'.'+ip_parts[2]+'.'

first_host = int(input("Enter first number: "))
last_host = int(input("Enter last number: "))
last_host += 1

oper = platform.system()

if (oper == "Windows"):
    ping = "ping -n 1 "
else:
    ping = "ping -c 1 -i 1 "

time1 = datetime.datetime.now()
print("Scanning in progress")

for ip in range(first_host, last_host):
    addr = network_ip + str(ip)
    command = ping + addr
    response = os.popen(command)
    print(ip)
    list = response.readlines()

    for line in list:
        if (line.count("ttl=")):
            print(addr, "--> live")
            break

time2 = datetime.datetime.now()
total = time2 - time1
print("Scan completed in ", total)
