# n과 m (5)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = list(map(int, input().split()))
number = sorted(number)
visited = [False] * N
answer = []

def dfs(n, lst):
    global answer
    if n == M:
        answer.append(lst)
        return
     
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            dfs(n+1, lst+[number[i]])
            visited[i]=False

dfs(0,[])
for i in answer:
    print(*i)