N = int(input())
# answer = len(list(combinations_with_replacement(range(10),N)))
answer = 1
for i in range(N+1, N+10):
    answer *= i
down = 1
for i in range(1,10):
    down *= i
answer = answer // down
print(answer % 10007)