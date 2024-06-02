
import sys
input = sys.stdin.readline

n = int(input())
word = input().strip()

if word.count('B') == 0 or word.count('R') == 0:
    answer = 0
else:
    # 1) 맨 뒤에 있는 색을 옮기는 경우
    string = word
    top = word[-1]
    while string[-1] == top:
        string = string[:-1]
    answer1 = string.count(top)

    # 2) 맨 뒤가 아닌 색을 옮기는 경우
    answer2 = n - word.count(word[-1])

    # 3) 맨 앞에 있는 색을 옮기는 경우
    string = word
    top = word[0]
    while string[0] == top:
        string = string[1:]
    answer3 = string.count(top)

    # 4) 맨 앞이 아닌 색을 옮기는 경우
    answer4 = n - word.count(word[0])
    
    answer = min(answer1, answer2, answer3, answer4)
print(answer)