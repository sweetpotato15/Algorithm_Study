import sys
input = sys.stdin.readline

# sol1) 다익스트라 - 각 지점들을 하나의 노드로 생각
# 1에서 2로 가는 거리 1
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (start, 0)) # (node, 거리)

    while q:
        node, dist = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n_node, n_dist in shortcut[node]: # 거쳐가는 경우
            if distance[n_node] > distance[node] + n_dist:
                distance[n_node] = distance[node] + n_dist
                heapq.heappush(q, (n_node, distance[n_node]))

N, D = map(int, input().split())
shortcut = [[] for _ in range(D+1)]

for _ in range(N):
    s, e, d = map(int, input().split())
    if e > D:
        continue
    shortcut[s].append([e, d])

for i in range(D):
    shortcut[i].append([i+1, 1])
distance = [INF]*(D+1) # 시작지점(0)부터 도착지까지 거리

dijkstra(0)
print(distance[-1])