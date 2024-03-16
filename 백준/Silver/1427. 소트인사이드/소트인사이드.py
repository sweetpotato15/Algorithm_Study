n = input()
number = []
for i in range(len(n)):
    number.append(int(n[i]))

number = sorted(number, reverse = True)

answer = ''
for i in range(len(n)):
    answer += str(number[i])
print(answer)