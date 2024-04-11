import sys
input = sys.stdin.readline

number = int(input())
total = [int(input()) for x in range(number)]
total.sort()

def roundUp(x):
    if (x - int(x)) >= 0.5:
        return int(x) + 1
    else:
        return int(x)
    
if number == 0:
    print(0)
else:
    n = roundUp(number * 0.15)
    if n == 0 :
        print(roundUp(sum(total)/len(total)))
    elif n + n >= number:
        print(0)
    else:
        print(roundUp(sum(total[n:-n]) / len(total[n:-n])))