import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
title = defaultdict(int)
for _ in range(N):
    word = input().strip()
    title[word] += 1
max_value = max(title.values())
answer = [i for i,j in title.items() if j == max_value]
print(sorted(answer)[0])