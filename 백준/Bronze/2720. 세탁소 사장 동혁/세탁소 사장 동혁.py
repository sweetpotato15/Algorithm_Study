
t = int(input())

A = [25,10,5,1]
for _ in range(t):
    value = int(input())
    for i in range(len(A)):
        if value >= A[i]:
            print(value // A[i], end=' ')
            value = value % A[i]
        else:
            print(0, end=' ')