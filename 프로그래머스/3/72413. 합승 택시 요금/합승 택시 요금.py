import heapq

# n : 전체 노드, s : 출발지점, a,b : 각 도착지점, fares : 요금
def solution(n, s, a, b, fares):
    global graph
    INF = 1e6
    graph = [[] for _ in range(n+1)]
    for i in fares:
        c,d,f = i
        graph[c].append([f,d]) # [거리요금, 도착지]
        graph[d].append([f,c])
    answer = dijkstra(s,a,n) + dijkstra(s,b,n)
    
    for i in range(1,n+1):
        if i == s:
            continue
        fare = dijkstra(s,i,n) + dijkstra(i,a,n) + dijkstra(i,b,n)
        answer = min(answer, fare)
    return answer

def dijkstra(start,end,n): # start에서 시작해서 end 까지의 최소비용
    INF = 1e6
    distance = [INF] * (n+1)
    q = [] # (거리, 노드)
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[0]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))            
    return distance[end]        

