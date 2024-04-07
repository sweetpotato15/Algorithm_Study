# 선행작업 -> 위상정렬
from collections import deque
import sys
import copy

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)


for i in range(1,n+1):
    array = list(map(int, input().split()))
    time[i] = array[0]
    indegree[i] = array[1]
    for j in array[2:]:
        graph[j].append(i)

def topology_sort():
    answer = time.copy()
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            answer[i] = time[i]
    
    while q:
        now = q.popleft()
        for i in graph[now] :
            indegree[i] -= 1
            answer[i] = max(answer[i], time[i]+answer[now])
            if indegree[i] == 0:
                q.append(i)
    print(max(answer))

topology_sort()