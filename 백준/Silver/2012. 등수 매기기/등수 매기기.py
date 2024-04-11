import sys
input = sys.stdin.readline

n = int(input()) # 총 학생 수
predict = [int(input()) for _ in range(n)]
predict.sort()
answer = list(range(1,n+1))

total = 0
for i in range(n):
    total += abs(predict[i] - answer[i])

print(total)
