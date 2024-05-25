import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
for i in range(n-1):
    if min_price <= price[i+1]:
        price[i+1] = min(price[i+1], min_price)
    else:
        min_price = price[i+1]

answer = 0
for i in range(n-1):
    answer += road[i] * price[i]
print(answer)