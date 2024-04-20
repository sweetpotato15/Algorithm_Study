import sys
input = sys.stdin.readline

n = int(input()) # 재료개수
m = int(input()) # 갑옷 만드는데 필요한 수
number = list(map(int, input().split()))
number.sort()

start = 0
end = n-1
count = 0

while start < end:
    value = number[start] + number[end]
    if value == m:
        start += 1
        end -= 1
        count += 1
    elif value < m :
        start += 1
    else:
        end -= 1

print(count)