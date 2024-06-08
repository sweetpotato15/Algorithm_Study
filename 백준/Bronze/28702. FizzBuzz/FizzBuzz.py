import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()

def string(num):
    if num % 3 == 0:
        if num % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    return num

if c.isdigit():
    print(string(int(c)+1))
elif b.isdigit():
    print(string(int(b)+2))
else:
    print(string(int(a)+3))