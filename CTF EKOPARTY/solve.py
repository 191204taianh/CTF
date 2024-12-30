# First, let's read the contents of the "julius" file to proceed with various decoding attempts.
import os
import zlib

print(os.getcwd())

file_path = r'C:\Users\ntanh\OneDrive\Documents\Code\CTF EKOPARTY\julius'

# Read the binary contents of the file
with open(file_path, 'rb') as file:
    file_contents = file.read()

# 1. Attempt Hexadecimal Interpretation
try:
    hex_interpretation = bytes.fromhex(file_contents.hex()).decode('ascii', errors='ignore')
except ValueError:
    hex_interpretation = None

# 2. Attempt Caesar Cipher on ASCII text
# Function to perform Caesar cipher on ASCII content
def caesar_decrypt(text, shift):
    decrypted_text = []
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            decrypted_text.append(chr((ord(char) - shift_base - shift) % 26 + shift_base))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

# Testing Caesar shifts on ASCII interpretation
caesar_results = []
for shift in range(1, 26):
    try:
        shifted_text = caesar_decrypt(file_contents.decode('ascii', errors='ignore'), shift)
        if "EKO{" in shifted_text:
            caesar_results.append((shift, shifted_text))
    except UnicodeDecodeError:
        continue

# 3. XOR Cipher Decryption
# Testing XOR with a single byte key (brute-force approach over all 256 possibilities)
xor_results = []
for key in range(256):
    xor_decrypted = bytes([b ^ key for b in file_contents])
    try:
        decoded_text = xor_decrypted.decode('ascii', errors='ignore')
        if "EKO{" in decoded_text:
            xor_results.append((key, decoded_text))
    except UnicodeDecodeError:
        continue

# 4. Check if it's compressed data (zlib decompression attempt)
try:
    decompressed_data = zlib.decompress(file_contents).decode('ascii', errors='ignore')
    if "EKO{" in decompressed_data:
        compression_result = decompressed_data
    else:
        compression_result = None
except zlib.error:
    compression_result = None

# Collect all results
results = {
    "hex_interpretation": hex_interpretation,
    "caesar_results": caesar_results,
    "xor_results": xor_results,
    "compression_result": compression_result
}

print(results)
