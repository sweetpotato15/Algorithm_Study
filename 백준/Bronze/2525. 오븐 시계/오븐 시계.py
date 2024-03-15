hour, min = map(int, input().split())
time = int(input())

plus_hour = time // 60
plus_min = time % 60

hour += plus_hour
min += plus_min

if min >= 60:
    hour += 1
    min -= 60

if hour >= 24:
    hour -= 24

print(hour, min)