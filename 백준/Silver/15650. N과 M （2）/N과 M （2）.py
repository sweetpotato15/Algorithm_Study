import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

def dfs(n, start,lst):
    global answer
    if n == M:
        answer.append(lst)
        return 
    for i in range(start+1, N+1):
        dfs(n+1, i,lst+[i])

dfs(0,0,[])
for i in answer:
    print(*i)