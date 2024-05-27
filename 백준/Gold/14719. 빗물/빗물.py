import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))
# 내 좌우에 있는 최댓값 중 작은 것 - 나 만큼 빗물 생김

water = 0
for i in range(1,len(block)-1):
    now = block[i]
    value = min(max(block[:i]), max(block[i+1:]))
    if now < value :
        water += value - now
print(water)