import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = [input().strip() for _ in range(n)]
bo = [input().strip() for _ in range(m)]
answer = list(set(d).intersection(set(bo)))
answer.sort()
print(len(answer))
for i in answer:
    print(i)
