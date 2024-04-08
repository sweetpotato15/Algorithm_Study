a , b = map(int, input().split())

for i in range(min(a,b), 0,-1):
    if a % i == 0 and b % i == 0:
        answer1 = i
        break

answer2 = answer1 * (a // answer1) * (b // answer1)       
print(answer1)
print(answer2)