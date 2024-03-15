import sys
text = sys.stdin.readlines()

for data in text:
    a,b = map(int, data.split())
    print(a+b)