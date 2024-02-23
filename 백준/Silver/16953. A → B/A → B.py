a,b = map(int, input().split())

# b -> a


def AB(a,b):
    count = 0
    while a < b :

        if str(b)[-1] == "1":
            
            b = b//10
            count += 1

        elif b % 2 == 0 :
            b = b // 2 
            count += 1
        
        else:
            break

    if a == b:
        print(count + 1)        

    else:
        print(-1)

AB(a,b)