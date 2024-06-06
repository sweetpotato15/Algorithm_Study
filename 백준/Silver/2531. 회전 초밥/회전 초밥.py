import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]
new_belt = belt[:] + belt[:k]

result = 0
start, end = 0, k
while end <= len(new_belt)+1:
    now = new_belt[start:end]
    now_type = len(set(now)) # 초밥 종류 수
    now_coupon = [0 if c in now else 1] # 쿠폰이 몇개 포함되는지
    answer = now_type + now_coupon[0]

    result = max(result, answer)
    start += 1
    end += 1

print(result)