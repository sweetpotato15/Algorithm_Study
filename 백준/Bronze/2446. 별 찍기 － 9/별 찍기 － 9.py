N = int(input())

for i in range(N):
    print(' '*i + '*'*(2*N-1-2*i))

for i in range(1, N):
    print(' '*(N-i-1)+'*'*(2*i+1))