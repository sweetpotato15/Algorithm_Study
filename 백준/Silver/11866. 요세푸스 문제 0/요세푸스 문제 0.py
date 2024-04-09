n, k = map(int,input().split())

answer = []
q = list(range(1, n+1))
while q:
    for _ in range(k-1):
        q.append(q.pop(0))
    answer.append(str(q.pop(0)))
print("<"+", ".join(answer)+">")