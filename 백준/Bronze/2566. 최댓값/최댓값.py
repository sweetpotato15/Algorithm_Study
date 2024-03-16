A = [0] * 9
for i in range(9):
    A[i] = list(map(int, input().split()))

maxvalue = A[0][0]
max_col = 0
max_row = 0

for i in range(9):
    for j in range(9):
        if maxvalue < A[i][j]:
            maxvalue = A[i][j]
            max_row = i
            max_col = j
        
print(maxvalue)
print(max_row+1, max_col+1)