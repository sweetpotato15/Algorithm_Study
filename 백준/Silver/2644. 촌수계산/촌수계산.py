import sys
input = sys.stdin.readline
from collections import deque

'''
dfs 방법으로 t1에서 시작해서 t2 까지 도달하는 방법
'''
def dfs(start, end, count):
    global flag, answer
    if start == end:
        flag = True
        answer = count
        return 
    visited[start] = True

    for x in graph[start]:
        if not visited[x]:
            dfs(x, end, count+1)

N = int(input())
t1, t2 = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

flag = False
answer = 0
dfs(t1, t2, 0)
if flag:
    print(answer)
else:
    print(-1)