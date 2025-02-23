# Given integer array in the Java code
int_values = [
    1096770097, 1952395366, 1600270708, 1601398833,
    1716808014, 1734293296, 842413104, 1684157793
]

# Convert each integer back to 4 characters
decoded_password = ''.join(
    chr((num >> 24) & 0xFF) +
    chr((num >> 16) & 0xFF) +
    chr((num >> 8) & 0xFF) +
    chr(num & 0xFF)
    for num in int_values
)

# Construct the final flag
flag = f"picoCTF{{{decoded_password}}}"
print(flag)
