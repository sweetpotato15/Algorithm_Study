word = input().strip()
array = word.split('-')
answer = ''
for i in array:
    answer += i[0]
print(answer)