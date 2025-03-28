import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for i in range(T):
    r = 0 # reverse 연산 개수
    command = input().strip()
    n = int(input())
    array = input().strip().strip('[]')

    if len(array) == 0: 
        q = deque([])
    else:
        q = deque(list(map(int, array.strip().split(','))))

    if command.count('D') > n: # D 개수가 list 길이보다 클 때
        print('error')
        continue
    else:
        for j in command:
            if j == 'R':
                r+=1
            else:
                if r%2 == 0: # 짝수번 reverse + delete
                    q.popleft()
                else:
                    q.pop()
        if r%2 == 1:
            q.reverse()
    
    answer = map(str, list(q))
    answer = '[' + ','.join(answer) + ']'
    print(answer)