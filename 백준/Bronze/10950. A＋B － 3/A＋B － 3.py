n = int(input())
answer = []
for _ in range(n):
    a,b = map(int, input().split())
    answer.append(a+b)

for ans in answer:
    print(ans)