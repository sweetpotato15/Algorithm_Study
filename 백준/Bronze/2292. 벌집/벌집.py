n = int(input())

if n == 1:
    print(1)
else:
    count = 0
    while True:
        for i in range(0,n):
            if n >= (2+3*i+3*(i**2)):
                count += 1
            
            else:
                break
        break
    print(count+1)