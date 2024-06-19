import sys
input = sys.stdin.readline

N = int(input())
power, weight = [0]*N, [0]*N
for i in range(N):
    power[i], weight[i] = map(int, input().split())
answer = 0

def dfs(n, count):
    global answer
    if n == N: # 모든 계란 완료 
        answer = max(answer, count)
        return 
    
    if power[n] <= 0: # 현재 계란 깨진 경우 -> 다음 계란으로
        dfs(n+1, count)
    else:              # 현재 계란 안깨진 경우
        flag = False
        for j in range(N):
            if n == j or power[j] <= 0: # 상대방이 나거나, 상대방 계란이 깨진 경우
                continue
            flag = True
            power[n] -= weight[j]
            power[j] -= weight[n]
            dfs(n+1,count+int(power[n]<=0)+int(power[j]<=0)) # 계란 깨진 경우 count 증가
            power[n] += weight[j]
            power[j] += weight[n]  

        if not flag: # 현재 계란이 안깨졌는데, 나머지 계란들이 다 깨진 경우 (위의 for문에서 dfs 못간 경우)
            dfs(n+1, count) 


dfs(0,0)
print(answer)