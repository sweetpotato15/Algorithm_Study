import sys
input = sys.stdin.readline

n = int(input())
water = list(map(int,input().split()))
a = int(1e10)
answer = []

start = 0
end = n-1
# 찾아야하는 값이 정해져 있지 않고 0에 가장 가까운 수를 찾아야 하는 문제
# -> 0에 가장 가까운 수를 기준선으로 

# a를 기준으로 합한 결과 (value)와 비교해가면서
while start < end:
    value = abs(water[start]+water[end])
    if value < a :
        a = value
        answer = sorted([water[start],water[end]])
    
    if water[start] + water[end] < a:
        start += 1
    else:
        end -= 1
    
print(*answer)