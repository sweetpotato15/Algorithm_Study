import sys
input = sys.stdin.readline


S = int(input())
# 서로 다른 N개의 자연수를 합해서 S가 되게끔 하는 N의 최댓값
# 서로 다른 n개의 자연수 1,2,3,4,5,6 7 8 9 10  -> 55 

ans = 0
value = 0
for i in range(1, S+1):
    value += i
    ans += 1
    if value >S:
        break

if S == 1:
    ans = 2
print(ans-1)