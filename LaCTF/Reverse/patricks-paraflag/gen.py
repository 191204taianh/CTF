flag = "lactf{the_flag_got_lost_in_infinity}"

out = ""
print("Length of the flag = " + str(len(flag)))
mid = len(flag) // 2
print("mid = " + str(mid))
print("First flag mid: " + str(flag[:mid]))
print("Second flag mid: " + str(flag[mid:]))
for (a, b) in zip(flag[:mid], flag[mid:]):
    out += a + b
    print(out)
print(out)