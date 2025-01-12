def decode_wheelbarrow(text, wheel_size):
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            # Calculate shift based on position
            shift = i % wheel_size
            base = ord('A') if char.isupper() else ord('a')
            # Roll backwards to undo the wheelbarrow effect
            decoded = (ord(char) - base - shift) % 26
            result += chr(decoded + base)
        elif char.isdigit():
            # Handle numbers similarly
            shift = i % wheel_size
            decoded = (int(char) - shift) % 10
            result += str(decoded)
        else:
            # Keep special characters unchanged
            result += char
    return result

cipher = "60_ZMZ_GBWKNREM_KRA__LQM}WEPRGQL__Q_{RWW_M_KIAGPMNMRXDLM_FMWLDQ0BOIAMNPG"

# Try different wheel sizes
for size in [3, 5, 7, 10]:
    decoded = decode_wheelbarrow(cipher, size)
    if "uoftctf{" in decoded.lower():
        print(f"Wheel size {size}: {decoded}")