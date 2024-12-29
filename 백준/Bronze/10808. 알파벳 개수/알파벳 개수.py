string = input().strip()
for i in range(97, 123):
    count = string.count(chr(i))
    print(count, end=" ")