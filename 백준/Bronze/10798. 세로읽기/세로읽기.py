word = []

for _ in range(5):
    word.append(input())

word_len = [len(x) for x in word]

for i in range(5):
    word[i] += ' '*(max(word_len)-len(word[i]))

answer = ''
for i in range(max(word_len)):
    for j in range(5):
        answer += word[j][i]

answer = answer.replace(" ","")
print(answer)

