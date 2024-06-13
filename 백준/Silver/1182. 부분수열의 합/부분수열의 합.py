import sys
input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))
answer = 0

def dfs(n, count):
    global answer
    if n == N:
        if len(count)!=0 and sum(count) == S:
            answer += 1
        return 
    dfs(n+1, count) # n번째 값 선택 안하는 경우
    dfs(n+1, count + [array[n]]) # n번째 값 선택하는 경우


dfs(0,[])
print(answer)