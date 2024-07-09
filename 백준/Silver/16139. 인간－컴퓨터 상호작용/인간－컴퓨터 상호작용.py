import sys
input = sys.stdin.readline

S = input().strip()
count = [[0]*26 for _ in range(len(S)+1)]
count[1][ord(S[0])-97] += 1

for i in range(2, len(S)+1):
    count[i] = count[i-1][:]
    count[i][ord(S[i-1])-97] += 1

q = int(input())
for _ in range(q):
    a,l,r=input().split()
    answer = count[int(r)+1][ord(a)-97] - count[int(l)][ord(a)-97]
    print(answer)