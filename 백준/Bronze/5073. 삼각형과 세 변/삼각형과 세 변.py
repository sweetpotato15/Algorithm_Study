while True:
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if max(a,b,c) >= sum([a,b,c]) - max(a,b,c):
        print("Invalid")
    else:
        if len(set({a,b,c})) == 1:
            print("Equilateral")
        elif len(set({a,b,c})) == 2:
            print("Isosceles")
        else:
            print("Scalene")