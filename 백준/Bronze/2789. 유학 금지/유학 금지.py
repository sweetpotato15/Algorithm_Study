word = input().strip()
answer = ''
for i in word:
    if i in ['A', 'B', 'C', 'D', 'E', 'M', 'R', 'I', 'G']:
        continue
    answer += i
print(answer)