names: set[str] = set()
ips: set[str] = set()
all_names = list()
all_ips = list()

with open("./invalid_users.txt") as f:
    lines = f.readlines()
    for line in lines:
        username = ((line.split(" ")))[7]
        ip_number = ((line.split(" ")))[9]
        # names.add(str(username))
        # ips.add(str(ip_number))
        all_names.append(username)
        all_ips.append(ip_number)
koncowy_plik_names: dict = dict()
for nazwa in all_names:
    if nazwa not in koncowy_plik_names:
        koncowy_plik_names[nazwa] = int(1)
    else:
        x: list = koncowy_plik_names.get(nazwa) + 1
        koncowy_plik_names.update({nazwa: x})
koncowa_lista = dict(
    sorted(koncowy_plik_names.items(), key=lambda item: item[1], reverse=True)
)
for i, k in koncowa_lista.items():
    print(i, k)
