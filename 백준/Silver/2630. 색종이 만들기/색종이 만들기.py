import sys
input = sys.stdin.readline

def check_one_color(array):
    sum_value = 0
    cnt = 0
    for i in array:
        sum_value += sum(i)
        cnt += len(i)
        if sum_value != 0 and sum_value != cnt:
            return False
    if sum_value == 0:
        return 'white'
    else:
        return 'blue'

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue, white = 0, 0

q = [paper]
while q:
    array = q.pop()
    if check_one_color(array) == False:
        n = len(array)//2
        a1 = [i[:n] for i in array[:n]]
        a2 = [i[n:] for i in array[:n]]
        a3 = [i[:n] for i in array[n:]]
        a4 = [i[n:] for i in array[n:]]
        q.append(a1)
        q.append(a2)
        q.append(a3)
        q.append(a4)
    elif check_one_color(array) == 'white':
        white += 1
    else:
        blue += 1

print(white)
print(blue)