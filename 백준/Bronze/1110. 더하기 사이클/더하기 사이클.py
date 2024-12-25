N = input().strip()
answer = 0
value = N
while True:
    if int(value) < 10:
        value = "0" + value
    sum_value = sum(map(int, list(value)))

    value = value[-1] + str(sum_value)[-1]
    answer += 1

    if int(value) == int(N):
        break
print(answer)