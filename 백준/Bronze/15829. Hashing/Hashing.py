import sys
input = sys.stdin.readline

n = int(input())
string = input()

r = 31
M = 1234567891

answer = 0
for i in range(n):
    answer += (ord(string[i]) -96) * r ** i 
print(answer % M)