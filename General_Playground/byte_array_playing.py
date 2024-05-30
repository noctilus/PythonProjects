import binascii

# Create a bytearray (replace this with your actual bytearray)
byte_array = bytearray(b'\x12\x34\x56\x78')

# Convert the bytearray to a hexadecimal representation
hex_string = binascii.hexlify(byte_array).decode()

# Print the hexadecimal representation
print(hex_string)

b = hex(int.from_bytes(byte_array, 'little'))
print(b)