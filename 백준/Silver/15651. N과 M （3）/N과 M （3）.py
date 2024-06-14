import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

def dfs(n,lst):
    if n == M:
        answer.append(lst)
        return 
    for i in range(1, N+1):
        dfs(n+1, lst+[i])

dfs(0,[])

for i in answer:
    print(*i)