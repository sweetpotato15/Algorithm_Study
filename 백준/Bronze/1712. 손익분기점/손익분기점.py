A, B, C = map(int, input().split())

if C <= B:
    print(-1)
else:
    answer = A/(C-B)
    print(int(answer)+1)
