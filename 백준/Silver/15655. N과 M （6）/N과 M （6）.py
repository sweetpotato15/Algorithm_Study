# n과 m (6)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
answer = []

def dfs(n, lst):
    global answer
    if n == N:
        if len(lst) == M:
            answer.append(lst)
        return 
    
    dfs(n+1, lst+[number[n]])
    dfs(n+1, lst)

dfs(0,[])
for i in answer:
    print(*i)