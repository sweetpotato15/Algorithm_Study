N = int(input())
q1,q2,q3,q4 = 0,0,0,0
for _ in range(N):
    x,y = map(int, input().split())
    if x >0 :
        if y>0:
            q1 += 1
        elif y <0 :
            q4 += 1
    elif x <0 :
        if y >0 :
            q2 += 1
        elif y <0:
            q3 += 1

print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {N-q1-q2-q3-q4}')