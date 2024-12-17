import sys
input = sys.stdin.readline
'''
IOIOI 의 최대 길이를 반환 -> combination

sol1) 양끝 O제거하고, IO -> A 로 replace 
IOIOI -> AAI -> 2 (A개수-1 + I 여부)
IOIO -> AA -> 1 (A개수-1 + I 여부)
IOIOIOIIOII -> AAAIAII -> 3, 1

sol2) 양끝 O제거하고, O를 기준으로 split
OOIOIOIOIIOII -> IOIOIOIIOII -> I,I,I,I,II,II

sol3) IOI -> 1로 치환
1OI -> 2
2OI -> 3
'''

N = int(input())
M = int(input())
S = input().strip()

# N = 3
# M = 2
# S = 'IOIO'
S = S.replace('IO', 'A').replace('I', 'I ').replace('O', 'O ')
S = S.split()

ans = 0
count = []
for string in S:
    if 'OI' in string or not string:
        continue
    count.append(string.count('A')-1 + int('I' in string))

for num in count:
    if num >= N:
        ans += num - N + 1
print(ans)
