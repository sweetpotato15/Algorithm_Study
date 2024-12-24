import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(x, y):
    global answer
    if visited[x][y]:
        return 
    visited[x][y] = True

    if graph[x][y] == "X":
        return 

    elif graph[x][y] == "P":
        answer += 1

    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    
    
N, M = map(int, input().split())
graph = ["X"*(M+2)] 
for i in range(N):
    string = input().strip()
    if "I" in string:
        sx, sy = i+1, string.index("I")+1
    graph.append("X"+string+"X")
graph += ["X"*(M+2)]
visited = [[False]*(M+2) for _ in range(N+2)]

answer = 0
dfs(sx, sy)

if answer == 0:
    print("TT")
else:
    print(answer)