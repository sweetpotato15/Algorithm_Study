N = int(input())
answer = []
for _ in range(N):
  score = 0
  array = sorted(list(map(int, input().split())))
  if len(set(array)) == 1:
    score = 10000 + array[0] * 1000
  elif len(set(array)) == 2:
    score = 1000 + array[1] * 100
  else:
    score = array[2] * 100
  answer.append(score)
print(max(answer))