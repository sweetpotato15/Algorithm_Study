total = []
before = 0
for _ in range(4):
    a, b = map(int, input().split())   
    before = before-a+b
    total.append(before)
print(max(total))