word = input()
for i in range(26):
    print(word.find(chr(97+i)), end= ' ')
