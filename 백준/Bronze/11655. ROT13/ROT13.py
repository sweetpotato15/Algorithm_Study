n = input()
for i in n:
    if 97 <= ord(i) <= 122:
        a = ord(i)
        a += 13
        if a > 122:
            a -= 26
        print(chr(a) , end='')
    elif 65 <= ord(i) <= 90:
        a = ord(i) 
        a += 13
        if a > 90:
            a -= 26
        print(chr(a), end='')
    elif i == " ":
        print(" ", end = '')
    else:
        print(i, end='')
print()