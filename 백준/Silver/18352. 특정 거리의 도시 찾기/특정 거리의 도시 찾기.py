import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
distance = [INF] * (n+1)    

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for node, value in graph[now]:
            cost = value + dist
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

dijkstra(x)

answer = [i for i in range(1, n+1) if distance[i] == k]

if not answer:
    print(-1)
else:
    for i in answer:
        print(i)
