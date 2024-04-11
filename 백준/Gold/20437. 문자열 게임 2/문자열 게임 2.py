import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    word = input()
    k = int(input())
    # word = "superaquatornado"
    # k=2
    answer = []
    word_count = [(i, word[i]) for i in range(len(word)) if word.count(word[i]) >= k]
    word_count = sorted(word_count, key = lambda x : x[1])
    for i in range(0,len(word_count)-k+1):
        if word_count[i][1] == word_count[i+k-1][1]:
            answer.append(word_count[i+k-1][0] - word_count[i][0]+1)
    if not answer:
        print(-1)
    else:
        print(min(answer), max(answer))
