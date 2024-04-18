import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
number.sort()

def Possible(number,x):
    start = 0
    end = len(number) - 1
    while start < end:
        value = number[start] + number[end]
        if value == x:
            return True
        elif value > x:
            end -= 1
        else:
            start += 1
    return False

count = 0
for i in range(n):
    array = number.copy()
    array.remove(number[i])
    if Possible(array, number[i]) == True:
        count += 1

print(count)