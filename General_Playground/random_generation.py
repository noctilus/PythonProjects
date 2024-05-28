#!/usr/bin/env python3

"""
Random string generator, with user specified length.

Taking num of chars - int, alphanumeric-Bool, special chars-Bool.
"""

# 33 -> 47 special
# 48 -> 57 0-9
# 58 -> 64 special
# 65 -> 90 A-Z
# 91 -> 96 special
# 97 -> 122 a-z
# 123 -> 126 special

import random
import time

chars_number = int(input("Chars number."))
# alpha_numeric = input("alphanumeric?")
# special_chars = input("Special Chars?")

print(chars_number)

print(f"Generating string {chars_number} characters long, ")


def randomness_generator(leng):
    """Generate string of leng length."""
    resulting_string = []

    while len(resulting_string) < leng:
        character = (random.randrange(33, 123))

        if 32 < character < 48:
            # exclude special chars
            # print(character, sep="", end="")
            # print(" rerandomizing")
            pass
        if 57 < character < 65:
            pass
        if 90 < character < 97:
            pass

        else:
            resulting_string.append(chr(character))
    return resulting_string


a = randomness_generator(chars_number)  # , alphannum=True, specialchars=True)
print(a)
print("-" * 20)
print("Printing one by one")
z = ""
z = z.join(a)
print(z)
for number in range(int(chars_number)):
    time.sleep(1 / 50)
    print(z[0:number], end="\r")
print(z)
print("")
