# Given scrambled flag
scrambled_flag = "l_alcotsft{_tihne__ifnlfaign_igtoyt}"

# Splitting into an array of individual characters
char_array = list(scrambled_flag)

# Display the array
print(char_array)
flag = ''
for i in range(0, len(char_array), 2):
    # Swap the characters
    temp = char_array[i]
    char_array[i] = char_array[i + 1]
    char_array[i + 1] = temp
    print(temp)
    flag += temp
    print(flag)