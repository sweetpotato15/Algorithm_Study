import sys
import heapq

input = sys.stdin.readline

# 정점, 간선의 개수
v, e = map(int, input().split())
start = int(input())
# 그래프
graph = [[] for _ in range(v+1)]
for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# 최단 경로 저장할 리스트
INF = int(1e9)
distance = [INF] * (v+1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start)) # (거리, 노드)
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])