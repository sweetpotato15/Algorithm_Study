a, b = map(int, input().split())
a5 = str(a).replace('6', '5')
a6 = str(a).replace('5', '6')
b5 = str(b).replace('6', '5')
b6 = str(b).replace('5','6')

print(int(a5)+int(b5), end=' ')
print(int(a6)+int(b6))