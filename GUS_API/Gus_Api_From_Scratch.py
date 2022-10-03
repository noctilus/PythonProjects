""" Api GUS Playground testing """
from gusregon import GUS

USER_KEY = "b71c1c32f1e745f5b305"

gus = GUS(api_key=USER_KEY)
informacja = gus.search(nip="8421582044")

for key, value in informacja.items():
    print(key, " : ", value)
