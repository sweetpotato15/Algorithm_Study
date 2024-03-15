hour, min = map(int, input().split())
if hour == 0:
    if min < 45:
        print(23, 60+min-45)
    else:
        print(hour, min-45)
else:
    if min < 45:
        print(hour-1, 60+min-45)
    else:
        print(hour, min-45)