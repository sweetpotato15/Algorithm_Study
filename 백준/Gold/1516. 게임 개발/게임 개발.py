from collections import deque
import sys
import copy

input = sys.stdin.readline

n = int(input())
time = [0]*(n+1)
indegree = [0] *(n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    array = list(map(int, input().split()))
    time[i] = array[0]
    for j in array[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

def topology_sort():
    result = copy.deepcopy(time) # 정답 저장할 리스트
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q :
        now = q.popleft()
        for i in graph[now]: # now 를 선수과목 가지고 있는 애들
            indegree[i] -= 1
            # 선행 건물이 여러개라면 더 오래 걸리는 선행 건물의 최소시간으로 업데이트
            result[i] = max( result[i], result[now] + time[i] )
            if indegree[i] == 0:
                q.append(i)

    for t in result[1:]:
        print(t)

topology_sort()
