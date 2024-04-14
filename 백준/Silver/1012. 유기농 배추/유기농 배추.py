import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for _ in range(t):
    n,m,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, input().split())
        graph[a][b] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                answer+= 1
    print(answer)