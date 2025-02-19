## Decoding the Encoded String in picoCTF Challenge

### **Understanding the Encoding Process**
The encoding process used the following Python expression:

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

1. `ord(flag[i])` – Converts each character in `flag` to its Unicode (ASCII) integer value.
2. `(ord(flag[i]) << 8) + ord(flag[i + 1])` –  
   - Shifts the first character's value 8 bits to the left (multiplying by 256).
   - Adds the second character’s value.
   - This results in a single integer that represents two ASCII characters combined.
3. `chr(...)` – Converts the integer back into a Unicode character.
4. The process repeats for every two characters in `flag`, and they are joined together to form a new string.

This transformation created the encoded string:  
```
"灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"
```
where each Unicode character holds two original ASCII characters.

---

### **Reversing the Encoding (Decoding)**
Now, let’s decode it:

```python
encoded = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"

decoded = ''.join(
    [chr((ord(c) >> 8) & 0xFF) + chr(ord(c) & 0xFF) for c in encoded]
)

print(decoded)
```

#### **Step-by-Step Breakdown**
1. **Extract Unicode integer values:**
   - `ord(c)` converts each character in `encoded` back to its integer representation.
   
2. **Reverse the bitwise transformation:**
   - `ord(c) >> 8` extracts the **high byte** (first character from encoding).
   - `ord(c) & 0xFF` extracts the **low byte** (second character).
   
3. **Convert back to characters:**
   - `chr((ord(c) >> 8) & 0xFF)` converts the high byte into a character.
   - `chr(ord(c) & 0xFF)` converts the low byte into a character.
   - The two characters are concatenated.

4. **Reconstruct the original flag:**  
   - The process repeats for every Unicode character in `encoded`, yielding the original ASCII string.

### **Example Calculation**
Let's take one Unicode character from the encoded string:

```python
ord("灩")  # This gives an integer value
```
Now, extract the original characters:

```python
high_byte = (ord("灩") >> 8) & 0xFF
low_byte = ord("灩") & 0xFF

chr(high_byte) + chr(low_byte)
```
This will produce the first two characters of the original flag.

---

### **Final Output**
When the script runs, it reveals the original flag in the format:

```
picoCTF{...}
```

This method effectively **reverses** the encoding process, restoring the original flag from its encoded Unicode representation. 🚀
