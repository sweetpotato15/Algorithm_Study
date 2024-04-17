import sys
input = sys.stdin.readline

t = int(input())

house = [[0]*(15) for _ in range(15)]
house[0] = list(range(15))

def people(k,n): # k층 n호
    global house
    for i in range(1,k+1):
        for j in range(1,n+1):
            house[i][j] = house[i][j-1] + house[i-1][j]
    print(house[k][n])

for _ in range(t):
    k = int(input())
    n = int(input())
    people(k,n)