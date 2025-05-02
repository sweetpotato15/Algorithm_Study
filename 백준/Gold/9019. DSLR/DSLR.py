import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def get_result(num, command):
    if command == 'D':
        return (num*2) % 10000
    if command == 'S':
        return num-1 if num!=0 else 9999
    if command == 'L':
        return (num%1000)*10 + num//1000
    else:
        return (num%10)*1000 + num//10

T = int(input())
for _ in range(T):
    start, end = map(int, input().split())
    dict = defaultdict(str)
    dict[start] = ''
    q = deque([start])
    
    while q:
        num = q.popleft()
        if num == end:
            break
        for i in ['D', 'S', 'L', 'R']:
            result = get_result(num, i)
            if result not in dict:
                q.append(result)
                dict[result] = dict[num] + i
    print(dict[end])