import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

def dfs(n,lst,now):
    global answer
    if n == M:
        answer.append(lst)
        return 
    for i in range(now, N+1):
        dfs(n+1, lst+[i], i)

dfs(0,[],1)
for i in answer:
    print(*i)