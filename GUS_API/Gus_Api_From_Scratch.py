""" Api GUS Playground testing """
from gusregon import GUS

nip_input = input("Podaj NIP szukanej firmy: ")
USER_KEY = "b71c1c32f1e745f5b305"

gus = GUS(api_key=USER_KEY)
informacja = gus.search(nip=nip_input)

for key, value in informacja.items():  # type: ignore
    print(key, " : ", value)
