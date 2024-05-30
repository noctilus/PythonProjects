names = set()
ips = set()

with open("./invalid_users.txt") as f:
    lines = f.readlines()
    for line in lines:
        username = ((line.split(" ")))[7]
        ip_number = ((line.split(" ")))[9]
        names.add(str(username))
        ips.add(str(ip_number))

for ip in ips:
    print(names)
# print(line)
