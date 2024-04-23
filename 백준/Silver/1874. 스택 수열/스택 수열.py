import sys
input = sys.stdin.readline

n = int(input())
answer = [int(input()) for _ in range(n)]

stack = []
result = ""
num = 1
flag = True
for i in range(n):
    now = answer[i]
    if now >= num:
        while now >= num:

            stack.append(num)
            result += "+\n"
            num += 1
        stack.pop()
        result += "-\n"
    else:
        n = stack.pop()
        if n > now:
            print("NO")
            flag = False
            break
        else:
            result += "-\n"
if flag:
    print(result)