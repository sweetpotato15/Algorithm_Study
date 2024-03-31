import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int, input().split())

def dijkstra(start,end):
    distance = [INF] * (n+1)
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
                heapq.heappush(q,(cost, node))
    return distance[end]

value1 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
value2 = dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)

answer = min(value1, value2)
if answer >= INF:
    print(-1)
else:
    print(answer)