import sys
input = sys.stdin.readline

'''
dfs 방법으로 t1에서 시작해서 t2 까지 도달하는 방법
'''
def dfs(start, count):
    global flag
    visited[start] = True
    if start == t2:
        flag = True
        print(count)
        return 

    for x in graph[start]:
        if not visited[x]:
            dfs(x, count+1)

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
dfs(t1, 0)
if not flag:
    print(-1)