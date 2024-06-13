# 로또 - 백트래킹

import sys
input = sys.stdin.readline

def recur(n,lst):
    global answer
    if n == N:
        if len(lst) == 6:
            answer.append(lst)
        return 
    recur(n+1, lst+[lotto[n]]) # n번째 수 선택
    recur(n+1, lst) # n번째 수 선택 안함
    
while True:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break
    N = lotto[0]
    lotto = lotto[1:]
    answer = []
    recur(0,[])
    for i in answer:
        print(*i)
    print()