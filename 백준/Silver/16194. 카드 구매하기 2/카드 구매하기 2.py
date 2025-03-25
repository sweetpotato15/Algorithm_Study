import sys
input = sys.stdin.readline

N = int(input())
card = [1000] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, i):
        card[i] = min(card[i], card[j]+card[i-j])

print(card[-1])
