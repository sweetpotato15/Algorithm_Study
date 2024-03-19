n = int(input())

f = [0] * (n+1)
answer2 = 0

f[1] = 1
f[2] = 1

for i in range(3, n+1):
  f[i] = f[i-1] + f[i-2]
  answer2 += 1

print(f[n], answer2)