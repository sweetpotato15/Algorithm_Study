string = input().strip()
ans = 10
prev = string[0]
for i in range(1,len(string)):
    if prev == string[i]:
        ans += 5
    else:
        ans += 10
    prev = string[i]
print(ans)