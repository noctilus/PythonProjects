import geocoder

all_names: list[str] = []
all_ips: list[str] = []
koncowy_plik_geo = list()
koncowy_plik_ips: dict[str, int] = {}

with open("./invalid_users.txt") as f:
    lines = f.readlines()
    for line in lines:
        username = ((line.split(" ")))[7]
        ip_number = ((line.split(" ")))[9]
        all_names.append(username)
        all_ips.append(ip_number)
for ip in all_ips:
    if ip not in koncowy_plik_ips:
        koncowy_plik_ips[ip] = int(1)
    else:
        x: int = koncowy_plik_ips.get(ip)
        x += 1
        koncowy_plik_ips.update({ip: x})
for ip, qtty in koncowy_plik_ips.items():
    try:
        geo = geocoder.ip(ip)
        x = geo, ip, qtty

        koncowy_plik_geo.append(x)
    except ValueError:
        pass

print(koncowy_plik_geo)


# koncowa_lista = dict(
# sorted(koncowy_plik_ips.items(), key=lambda item: item[1], reverse=False)
# )
# for i, k in koncowa_lista.items():
# print(i, k)
