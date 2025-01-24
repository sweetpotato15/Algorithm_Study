array=[]
for i in range(7):
    num = int(input())
    if num%2==1:
        array.append(num)

if array:
    print(sum(array))
    print(min(array))
else:
    print(-1)