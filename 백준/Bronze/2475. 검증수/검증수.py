number = list(map(int, input().split()))
s = 0
for i in number:
    s += i **2
print(s % 10)