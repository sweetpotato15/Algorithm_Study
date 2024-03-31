import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance = [INF] * (n+1)

def dijkstra( start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0,start))
    while queue:
        dist, now = heapq.heappop(queue)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(1)

print(distance[-1])