import numpy as np

def analyze_measurements(qubits, bases, measurements):
    """
    Analyze the pattern of correct and incorrect measurements to identify the key.
    """
    key_bits = []
    errors = []
    
    # Find positions where measurements are available (not ?)
    valid_positions = [i for i, m in enumerate(measurements) if m != '?']
    
    # Compare measurements with original qubits
    for i in valid_positions:
        if bases[i] == 'R':  # Only consider matching bases
            expected = qubits[i]
            actual = measurements[i]
            if expected != actual:
                errors.append(i)
            key_bits.append(expected)
    
    # Analyze error pattern
    error_intervals = [errors[i+1] - errors[i] for i in range(len(errors)-1)]
    return key_bits, errors, error_intervals

def find_potential_seed(encrypted_msg, key_bits):
    """
    Try to find the seed used for the PRNG in the encryption.
    """
    # Convert encrypted message to binary
    msg_binary = []
    for byte in encrypted_msg:
        msg_binary.extend([int(bit) for bit in format(byte, '08b')])
    
    # XOR with known key bits to get potential original message bits
    potential_msg = []
    for i in range(min(len(key_bits), len(msg_binary))):
        potential_msg.append(msg_binary[i] ^ key_bits[i])
    
    return potential_msg

# Process the given data
qubits = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1]
bases = ['R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'R', 'D', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'D', 'R', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'D', 'D']
measurements = [0, 1, '?', 1, 0, '?', 1, 1, '?', 0, 1, '?', 0, 1, '?', 0, 1, '?', 1, 0, '?', 1, 0, '?', 0, 1, '?', 0, 1, '?', 1, 0, '?', 0, 0, '?', 0, 1, '?', 0, 1, '?', 1, 1, '?', 1, 0, '?', 1, 0, '?', 0, 1, '?', 0, 1, '?', 0, 1, '?', 1, 0, '?', 1, 0, '?', 0, 1, '?', 0, 0, '?', 0, 1, '?', 1, 1]
encrypted_msg = [0x23, 0x59, 0x86, 0x1e, 0x60, 0xcf, 0xdc, 0x4e, 0x6a, 0x0b, 0x0c, 0x50, 0xd4, 0x5a, 0x71, 0x87, 0xdb, 0x0c, 0x46, 0x1d, 0x63, 0x44, 0xba, 0x5e, 0x37, 0xd3, 0x9a, 0x4b, 0x77, 0x4b, 0x3d, 0x4b]

# Analyze the measurements
key_bits, errors, error_intervals = analyze_measurements(qubits, bases, measurements)

# Find potential original message
potential_msg = find_potential_seed(encrypted_msg, key_bits)

print("Error positions:", errors)
print("Error intervals:", error_intervals)
print("Number of key bits recovered:", len(key_bits))
print("First few key bits:", key_bits[:20])
print("First few potential message bits:", potential_msg[:20])