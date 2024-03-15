answer = []
for _ in range(10):
    a = int(input())
    answer.append(a%42)

print(len(set(answer)))
