N,B = map(int, input().split())

answer = []

while N != 0:
    answer.append(N%B)
    N = (N - N%B) // B

result = []
for i in answer:
    if i >= 10:
        result.append(chr(i + 55))
    else:
        result.append(i)

result.reverse()

for i in result:
    print(i, end='')
