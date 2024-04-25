import sys
input = sys.stdin.readline
from bisect import bisect_right, bisect_left

N, target = map(int, input().split())
A = list(map(int, input().split()))

# 수열 합이 구하고자 하는 것보다 작을 때
if sum(A) < target: answer = 0

# 수열 합이 구하고자 하는 것과 같을 때
elif sum(A) == target: answer = N

# 수열의 최댓값 혹은 최솟값이 구하고자 하는 것보다 클 때
elif max(A) >= target or min(A) >= target: answer = 1

else: # 그 외의 경우
    S = [0] * N # 부분합 0 ~ i 까지의 합
    S[0] = A[0]
    for i in range(1, N):
        S[i] = S[i-1] + A[i]
    answer = bisect_left(S,target)+1 # answer 번째 인덱스에 target 이 들어가야함
    for i in range(answer-1, N):
        new_index = bisect_right(S, S[i] - target) - 1
        answer = min(answer, i-new_index)
            
print(answer)