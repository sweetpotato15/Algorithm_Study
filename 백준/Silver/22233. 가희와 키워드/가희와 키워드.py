import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n : 키워드 수, m : 글 수 
dict1 = {}

for i in range(n):
    dict1[input().strip()] = 1
for i in range(m):
    new = list(input().strip().split(','))
    for j in new:
        if j in dict1.keys():
            del dict1[j]
    print(len(dict1))