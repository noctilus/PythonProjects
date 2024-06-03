names = set()
ips = set()
all_names = list()
all_ips = list()

with open("./invalid_users.txt") as f:
    lines = f.readlines()
    for line in lines:
        username = ((line.split(" ")))[7]
        ip_number = ((line.split(" ")))[9]
        names.add(str(username))
        ips.add(str(ip_number))
        all_names.append(username)
        all_ips.append(ip_number)

print(len(all_ips))

print(len(all_names))
names_list = sorted(names)
ips_list = sorted(ips)

print(f"Ilość usernames: {len(names_list)}")
print(f"Ilość IP: {len(ips_list)}")
