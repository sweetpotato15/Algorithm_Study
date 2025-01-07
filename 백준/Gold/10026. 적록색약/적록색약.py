import sys
input = sys.stdin.readline
from copy import deepcopy
sys.setrecursionlimit(int(1e9))

N = int(input())

graph = [['X']*(N+2)]+[['X']+list(input().strip())+['X'] for _ in range(N)]+[['X']*(N+2)]

def main(graph):
    visited = [[True]*(N+2)]+[[True]+[False]*N+[True] for _ in range(N)]+[[True]*(N+2)]
    answer = {'R':0, 'G':0, 'B':0}
    for i in range(1, N+1):
        for j in range(1, N+1):
            color(graph, visited, i, j, graph[i][j])

            if flag:
                answer[flag] += 1
    print(sum(answer.values()), end=" ")

def color(graph, visited, x, y, c):
    global flag
    # 이미 방문했거나 색이 다른 경우 return 
    if visited[x][y] or graph[x][y]!=c:
        flag = False
        return 
    graph[x][y] = "X"
    visited[x][y] = True
    for i,j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nx, ny = x+i, y+j
        # 인접점 중에서 방문하지 않고 color가 같은 경우 재귀귀
        if not visited[nx][ny] and graph[nx][ny] == c:
            color(graph, visited, nx, ny, c)

    flag = c

graph1 = deepcopy(graph)
graph2 = deepcopy(graph)
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph2[i][j] == "R":
            graph2[i][j] = "G"
main(graph1)
main(graph2)