import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostname(sys.argv[1])

else:
    print("Invalid number of arguments")
    print("Usage: python3 scanner.py <ip>")
    sys.exit()

# Add pretty banner
print("-"*25)
print("Scanning target "+target)
print("Time started: " + str(datetime.now()))
print("-"*25)