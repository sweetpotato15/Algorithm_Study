import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]
new_belt = belt[:] + belt[:k]

result = 0
start, end = 0, k
while end <= len(new_belt)+1:
    now = new_belt[start:end]
    # 연속된 접시 중 초밥 종류 + 쿠폰이 포함되는지 여부 (있으면 0, 없으면 1)
    answer = len(set(now)) + int(c not in now)
    result = max(result, answer)
    start += 1
    end += 1

print(result)