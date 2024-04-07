import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
def building():
    n,k  = map(int, input().split()) # n 건물개수, k 규칙 개수
    time = [0] + list(map(int, input().split())) # 건설 시간 i번째 건물 i 시간
    graph = [[] for i in range(n+1)]
    indegree = [0] *(n+1)
    for i in range(k):
        a, b = map(int, input().split()) # a-> b
        graph[a].append(b) 
        indegree[b] += 1
    goal = int(input())
    result = time.copy()

    q  = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], time[i] + result[now])
            indegree[i] -= 1

            if indegree[i] == 0 :
                q.append(i)
    print(result[goal])

for i in range(t):
    building()