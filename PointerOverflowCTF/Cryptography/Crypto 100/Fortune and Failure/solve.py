# Function to decrypt the message based on substitution logic
def decrypt_message(ciphertext):
    # Mapping from "hottx" -> "poctf", likely a shift pattern
    substitution_map = str.maketrans("hottx", "poctf")
    prefix = ciphertext[:5].translate(substitution_map)  # Transform prefix
    
    # Decrypt the body of the flag (analyzing shifts)
    body = ciphertext[6:-1]  # Extract the main body inside {}
    decrypted_body = body.translate(str.maketrans("hottx{unsh", "poctf{uwsp"))  # Apply mapping to body
    
    # Combine decrypted parts
    return f"{prefix}{{{decrypted_body}}}"

# Ciphertext provided
ciphertext = "hottx{unsh_4_w4ck_7zrfuyh_7y3_h1dl5}"

# Decrypt the message
decrypted_message = decrypt_message(ciphertext)
print(decrypted_message)
