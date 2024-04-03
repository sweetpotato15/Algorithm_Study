n = int(input())
wordlist = []
for i in range(n):
    word = input() 
    wordlist.append((len(word), word))

wordlist = list(set(wordlist))   
wordlist.sort()
for (a,b) in wordlist:
    print(b)