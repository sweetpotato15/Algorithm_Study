N = int(input())
honey = list(map(int, input().split()))
honey_sum = honey[:]

answer = 0
for i in range(N-1):
    honey_sum[i+1] += honey_sum[i]
total = honey_sum[-1]

# 꿀이 맨 왼쪽에 위치 - 한마리는 맨 오른쪽 
for bee2 in range(1,N-1):
    b1 = total - honey[bee2] - honey[-1]
    b2 = honey_sum[bee2-1]
    answer = max(answer,b1+b2)

# 꿀이 맨 오른쪽에 위치 - 한마리는 맨 왼쪽
for bee2 in range(1, N-1):
    b1 = total - honey[bee2] - honey[0]
    b2 = total - honey_sum[bee2]
    answer = max(answer, b1+b2)

# 꿀이 가운데 위치 - 벌을 양쪽끝에 고정시키고 꿀을 가운데서 이동
for h in range(1,N-1):
    b1 = honey_sum[h] - honey[0]
    b2 = honey_sum[-2] - honey_sum[h-1]
    answer = max(answer, b1+b2)
print(answer)