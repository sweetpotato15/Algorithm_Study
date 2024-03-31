import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start,end):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if dist > distance[now]:
            continue
        for node, value in graph[now]:
            cost = value + dist
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(queue, (cost, node))
    return distance[end]


answer = [0] * (n+1)
for i in range(1, n+1):
    answer[i] = dijkstra(i, x) + dijkstra(x,i)

print(max(answer))