import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

chicken = []
home = []
for i in range(N):
    command = list(map(int, input().split()))
    for j in range(N):
        if command[j] == 2:
            chicken.append([i, j])
        elif command[j] == 1:
            home.append([i, j])

# 치킨집에서 집까지 거리 abs 사용해서 더하기 
result = []
for i in range(1, M+1): # 치킨집 개수 1~M
    for index in combinations(chicken, i):
        sum_dist = 0
        for j in home: # 집 하나에 치킨집까지 거리를 각각 구해서 가장 작은 값 더하기기
            value = int(1e6)
            for k in range(i): # 치킨집 경우 개수
                value = min(value, abs(j[0]-index[k][0]) + abs(j[1]-index[k][1]))
            sum_dist += value
        result.append(sum_dist)

print(min(result))
                
