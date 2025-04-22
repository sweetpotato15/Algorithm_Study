import sys
input = sys.stdin.readline

def check_strike(num, ans):
    s = 0
    for i in range(3):
        if str(num)[i] == str(ans)[i]:
            s += 1
    return s

def check_ball(num, ans):
    b = 0
    num = list(str(num))
    ans = list(str(ans))
    for i in range(3):
        if num[i] in ans and num[i] != ans[i]:
            b += 1
    return b

N = int(input())
array = [False]*100 + [True]*900 # (0~99 + 100~999)
for _ in range(N):
    num, s, b = map(int, input().split())
    for i in range(100, 1000): # 100~999
        if array[i]:
            if check_strike(i, num) == s and check_ball(i, num) == b:
                continue
            else:
                array[i] = False

answer = 0
for i in range(100, 1000):
    if array[i] and len(set(list(str(i)))) == 3 and '0' not in set(list(str(i))):
        answer += 1

print(answer)