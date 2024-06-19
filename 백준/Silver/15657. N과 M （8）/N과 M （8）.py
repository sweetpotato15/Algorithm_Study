import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array = sorted(list(set(array)))
answer = []

def dfs(n, lst, last):
    global answer
    if n == M:
        answer.append(lst)
        return 
    for i in range(last, N):
        dfs(n+1, lst+[array[i]],i)

dfs(0,[],0)
for i in answer:
    print(*i)