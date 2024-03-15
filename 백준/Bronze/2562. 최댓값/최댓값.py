arr1 = []
for i in range(1,10):
    arr1.append(int(input()))

print(max(arr1))
print(arr1.index(max(arr1)) + 1)