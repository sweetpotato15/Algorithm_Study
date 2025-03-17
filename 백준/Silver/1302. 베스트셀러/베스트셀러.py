import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
title = defaultdict(int)
for _ in range(N):
    word = input().strip()
    title[word] += 1
value = list(title.values())
max_value = sorted(value)[-1]
answer = [i for i,j in title.items() if j == max_value]
print(sorted(answer)[0])