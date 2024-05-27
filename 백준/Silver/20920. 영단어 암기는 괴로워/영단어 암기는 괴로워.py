import sys
input = sys.stdin.readline

n,m = map(int, input().split())
words = {}
for i in range(n):
    word = input().strip()
    if len(word) >= m:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

answer = []
words = list(words.items())
for i in range(len(words)):
    a,b = words[i]
    answer.append([b,len(a), a])
answer = sorted(answer, key = lambda x : (-x[0], -x[1], x[2]))
for i in answer:
    print(i[-1])