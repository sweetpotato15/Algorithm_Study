import sys
input = sys.stdin.readline

target = input().strip()
answer = 1

while True:
    string = str(answer)
    while string and target:
        if string[0] == target[0]:
            target = target[1:]
        string = string[1:]
    if not target:
        print(answer)
        break
    answer += 1