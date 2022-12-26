#! /bin/python3
"""Character conversion script."""
from tabulate import tabulate

tabulation_data = []

character = input('Input single character to convert: ')
for letter in character:
    tabulation_data.append(('ASCII:', (ascii(letter))))
    tabulation_data.append(("UNICODE:", (ord(letter))))
    tabulation_data.append(('BIN of UNICODE', (bin(ord(letter)))))
    tabulation_data.append(("OCT of UNICODE:", (oct(ord(letter)))))
    tabulation_data.append(('HEX of UNICODE:', (hex(ord(letter)))))
    tabulation_data.append(('Hash:', (hash(letter))))
    tabulation_data.append(('--------------- ', '---------------'))
if isinstance(character, int):
    print("CHR:", (chr(character)))
    print("HEX:", (hex(character)))
else:
    print('CHR: N/A')
    print('UNICHR: N/A')
    print('HEX: N/A')

print(tabulate(tabulation_data))
