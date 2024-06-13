import sys
input = sys.stdin.readline

n = int(input())
card = [0] + list(map(int, input().split()))

for i in range(2, n+1): # i원을 만들어야함
    value = 0
    for j in range(i//2+1):
        value = max(value, card[i-j]+card[j])

    card[i] = max(card[i], value)
print(card[-1])