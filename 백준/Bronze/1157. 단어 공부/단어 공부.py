word = input().upper()
wordlist = []
for i in range(len(word)):
    wordlist.append(word[i])
wordlist = list(set(wordlist))

answer = []
for i in wordlist:
    answer.append(word.count(i))

if answer.count(max(answer)) >= 2:
    print("?")
else:
    print(wordlist[answer.index(max(answer))])