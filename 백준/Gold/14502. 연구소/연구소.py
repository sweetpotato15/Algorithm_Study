import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
graph = []
virus = [] # 바이러스 좌표 
zero = []
maximum = 0

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] == 2:
            virus.append((i, j))
        elif lst[j] == 0:
            zero.append((i, j))
    graph.append(lst)

def count_virus(graph):
    q = deque(virus)

    while q:
        x, y = q.popleft()
        if graph[x][y] != 2:
            continue
        for i, j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x+i, y+j
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 2
    return graph

def count_zero(graph):
    ans = 0
    for i in graph:
        ans += i.count(0)
    return ans

for idx in list(combinations(range(len(zero)),3)):
    graph_copy = deepcopy(graph)
    for i in idx:
        graph_copy[zero[i][0]][zero[i][1]] = 1
    new_graph = count_virus(graph_copy)
    cnt = count_zero(new_graph)
    if cnt > maximum:
        maximum = cnt

print(maximum)