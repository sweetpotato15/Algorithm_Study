x = []
y = []

for _ in range(3):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
answer_x = 0
answer_y = 0
for i in range(3):
    if x.count(x[i]) == 1:
        answer_x = x[i]
    if y.count(y[i]) == 1:
        answer_y = y[i]

print(answer_x, answer_y)
