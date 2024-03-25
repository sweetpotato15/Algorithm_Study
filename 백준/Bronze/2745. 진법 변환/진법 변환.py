n, b = input().split()
b = int(b)
answer = 0
for i in range(len(n)):
    if ord(n[i]) < 65:
        answer += int(n[i]) * (b ** (len(n)-i-1))
    else:
        answer += (ord(n[i]) - 55) * (b **(len(n)-i-1))

print(answer)