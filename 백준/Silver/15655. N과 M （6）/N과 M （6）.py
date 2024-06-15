# n과 m (6)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
answer = []

def dfs(n, lst, start):
    global answer
    if n == M:
        answer.append(lst)
        return 
    
    for i in range(start, N):
        dfs(n+1, lst+[number[i]], i+1)

dfs(0,[],0)
for i in answer:
    print(*i)