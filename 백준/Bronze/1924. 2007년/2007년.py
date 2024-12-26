X, Y = map(int, input().split())
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
answer = sum(day[:X-1]) + Y -1
print(date[answer%7])