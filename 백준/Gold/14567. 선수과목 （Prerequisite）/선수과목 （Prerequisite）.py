from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(1, m+1):
    a,b = map(int, input().split())
    graph[a].append(b) # a가 b의 선수
    indegree[b] += 1

def topology_sort():
    q = deque()
    semester = [0] * (n+1)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            semester[i] = 1
    
    while q:
        now = q.popleft()
        for v in graph[now]:
            indegree[v] -= 1
            semester[v] = semester[now] + 1
            if indegree[v] == 0:
                q.append(v)
    
    print(*semester[1:])

topology_sort()