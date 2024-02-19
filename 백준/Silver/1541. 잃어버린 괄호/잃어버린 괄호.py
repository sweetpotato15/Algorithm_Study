message = input()

no_minus = message.split("-") 

answer = []

for i in no_minus:
    if "+" in i:
        plus = i.split("+")
        plus = [int(x) for x in plus]
        answer.append(sum(plus))
    else:
        answer.append(int(i))

cal = answer[0]

for i in range(1,len(answer)):
    cal -= answer[i]
print(cal)