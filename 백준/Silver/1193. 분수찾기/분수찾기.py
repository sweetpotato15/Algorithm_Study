n = int(input())

if n == 1:
    print("{}/{}".format(1,1))
else:
    count = 1

    for i in range(1,n+100):
        if n < 1 + i*(i-1)//2:        
            break
        start = 1 + i*(i-1)//2
        count = i

    if count % 2 == 0:
        left = n + 1 - start
        right = count + 1 - left
    else:
        right = n + 1 - start
        left = count + 1 - right

    print("{}/{}".format(left, right))