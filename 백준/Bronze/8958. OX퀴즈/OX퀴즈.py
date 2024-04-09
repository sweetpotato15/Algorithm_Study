t = int(input())
def score():
    word = input()
    answer = 0
    right = 0
    for i in range(len(word)):
        if word[i] == "O":
            right += 1
            answer += right
        else:
            right = 0
    print(answer)

for _ in range(t):
    score()