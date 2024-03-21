n = int(input())
m, k = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
answer_n = 0
answer_sum = 0

while answer_sum < m*k :
    answer_sum += A.pop()
    answer_n += 1
    if answer_sum >= m*k:
        print(answer_n)
        break
    if not A:
        print('STRESS')
        break
