n, k =map(int, input().split())

money = []
for i in range(n):
    money.append(int(input()))

money.sort(reverse = True)
count = 0

while k != 0:
    for value in money:
        if k >= value:
            count += k // value
            k = k % value


print(count)