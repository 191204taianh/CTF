
# **VaultDoor7 Password Decoding**

## **Step 1: Understanding the Encoding Mechanism**
- The password consists of **32 characters**.
- Each **group of 4 characters** is packed into a **single 32-bit integer** using bitwise operations:

    ```
    int_value = (char1 << 24) | (char2 << 16) | (char3 << 8) | char4
    ```

- Given **8 integers**, we can extract **4 characters per integer** to reconstruct the password.

---

## **Step 2: Given Encoded Integer Array**
From the Java program, we have the **encoded password stored as integers**:

```java
int_values = [
    1096770097, 1952395366, 1600270708, 1601398833,
    1716808014, 1734293296, 842413104, 1684157793
];
```

---

## **Step 3: Extracting Characters from Integers**
Each integer stores 4 characters. We **reverse the bit-shifting operation**:

1. **Extract the first character**:
    ```
    char1 = (int_value >> 24) & 0xFF
    ```

2. **Extract the second character**:
    ```
    char2 = (int_value >> 16) & 0xFF
    ```

3. **Extract the third character**:
    ```
    char3 = (int_value >> 8) & 0xFF
    ```

4. **Extract the fourth character**:
    ```
    char4 = (int_value) & 0xFF
    ```

Applying this method, we retrieve the following characters:

| Integer (Decimal) | Binary Representation | Extracted Characters |
|-------------------|----------------------|----------------------|
| **1096770097**   | `01000001 01011111 01100010 00110001` | `'A' '_' 'b' '1'` |
| **1952395366**   | `01110100 01011111 00110000 01100110` | `'t' '_' '0' 'f'` |
| **1600270708**   | `01100010 01101001 01110100 01011111` | `'b' 'i' 't' '_'` |
| **1601398833**   | `01110011 01101000 01101001 01100110` | `'s' 'h' 'i' 'f'` |
| **1716808014**   | `01110100 01001001 01101110 01100111` | `'t' 'I' 'n' 'g'` |
| **1734293296**   | `01110000 01101111 01110000 01101001` | `'p' 'o' 'p' 'i'` |
| **842413104**    | `00110011 00110100 00110000 00110100` | `'3' '4' '0' '4'` |
| **1684157793**   | `01110100 01101100 01100100 01100001` | `'t' 'l' 'd' 'a'` |

After concatenation, the **decoded password** is:

```
A_b1t_0f_b1t_sh1fTiNg_702640db5a
```

---

## **Step 4: Constructing the Final Flag**
Following the **picoCTF flag format**, we enclose the password within `{}`:

```
picoCTF{A_b1t_0f_b1t_sh1fTiNg_702640db5a}
```

---

## **Final Answer**

Flag: `picoCTF{A_b1t_0f_b1t_sh1fTiNg_702640db5a}`


