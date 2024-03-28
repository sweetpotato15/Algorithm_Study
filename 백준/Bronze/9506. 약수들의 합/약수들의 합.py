while True:
    n = int(input())
    if n == -1:
        break
    number = []
    for i in range(1,n):
        if n % i == 0:
            number.append(i)

    if sum(number) == n :
        print("{} =".format(n), end =" ")
        for i in number:
            if i == number[-1]:
                print("{}".format(i)) 
            else:                            
                print("{} +".format(i), end = ' ')
    
    else:
        print("{} is NOT perfect.".format(n))