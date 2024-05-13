import sys
input = sys.stdin.readline

n = int(input()) # 굴다리 개수
m = int(input()) # 가로등 개수
light = [0] + list(map(int, input().split())) + [n]
interval = 0

for i in range(1,m+2) :    
    value = (light[i] - light[i-1])
    if i != 1 and i != m+1:
        if value % 2 != 0:
            value = value // 2 + 1
        else: value = value//2
    interval = max(interval, value)

print(interval)