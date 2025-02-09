N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

answer = [A[i]*B[i] for i in range(N)]
print(sum(answer))