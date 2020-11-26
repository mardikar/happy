f = open('my_file', 'w+b')
byte_arr = [123, 124]
binary_format = bytearray(byte_arr)
f.write(binary_format)
f.close()

with open("my_file", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        # Do stuff with byte.
        byte = f.read(1)