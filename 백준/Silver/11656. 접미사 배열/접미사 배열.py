word = input().strip()

words = [word[i:] for i in range(len(word))]
print(*sorted(words), end='\n')