S = input().strip()

while '00' in S or '11' in S:
    S = S.replace('00','0')
    S = S.replace('11','1')

answer = min(S.count('0'), S.count('1'))
print(answer)