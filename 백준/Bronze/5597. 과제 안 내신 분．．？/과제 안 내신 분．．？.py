arr = []
number = [i for i in range(1,31)]
for _ in range(28):
    arr.append(int(input()))

absent = list(set(number).difference(set(arr)))
print(min(absent))
print(max(absent))