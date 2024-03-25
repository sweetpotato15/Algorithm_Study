n = int(input())
point = [0] * (n+1)
point[0] = 4
point[1] = 9
for i in range(2,n+1):
    length = 2**i
    point[i] = point[i-1] + ((2 **(2*i-2))*5 - (2**(i-1)-1)*2*(2**(i-1)))

print(point[n])