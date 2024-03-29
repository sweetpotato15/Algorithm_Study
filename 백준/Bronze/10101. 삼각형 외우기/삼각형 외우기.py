angle = []
for _ in range(3):
    angle.append(int(input()))

if sum(angle) == 180:
    if len(set(angle)) == 1:
        print("Equilateral")
    elif len(set(angle)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
