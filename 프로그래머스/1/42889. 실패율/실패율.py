
from bisect import bisect_left, bisect_right
def solution(N, stages):
    # 실패율 = 스테이지 도달했으나 클리어하지 못한 사람 수 / 스테이지에 도달 사람 수
    # 분자 : 스테이지 수, 분모 : 그 수 이상
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 반환
    fail = [0] * (N+1) 
    stages = sorted(stages) # 12223346
    for i in range(1, N+1):
        up = bisect_right(stages, i) - bisect_left(stages, i)
        down = len(stages) - bisect_left(stages, i)
        if down == 0:
            fail[i] = 0
            continue

        fail[i] = up/down
    fail = fail[1:]
    answer = sorted(enumerate(fail), key = lambda x : x[1], reverse = True)
    result = []
    for i in answer:
        result.append(i[0]+1)
    return result


# def solution(N, stages):
#     dp = [0] * (N+2)
#     for i in stages:
#         dp[i] += 1
#     fail = [0] *(N+1)
#     for i in range(N+1):
#         fail[i] = [i,dp[i] / sum(dp[i:])]
#     fail = fail[1:]
#     answer = sorted(enumerate(fail), key = lambda x : x[1], reverse = True)
#     result = []
#     for i in answer:
#         result.append(i[0]+1)
#     return result

   