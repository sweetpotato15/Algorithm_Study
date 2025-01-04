x = int(input())
array = [x**2 for x in range(1, int(50000**(1/2))+1)]

def square(x):
    if (x**(1/2)).is_integer():
        return 1
    else:
        for i in array:
            if x-i in array:
                return 2
        
        for i in range(len(array)):
            remainder = x-array[i]
            for j in range(i, len(array)):
                if remainder-array[j] in array:
                    return 3
        
    return 4

print(square(x))