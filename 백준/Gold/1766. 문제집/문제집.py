import sys
import heapq # deque 으로 하면 q에서 정렬을 못함

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q,i)
    while q:
        
        now = heapq.heappop(q)
        print(now, end=" ")
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q,i)
        
        
topology_sort()