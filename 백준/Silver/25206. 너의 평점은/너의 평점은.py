score = ['A+','A0','B+','B0','C+','C0','D+','D0','F']

score_num = 0
num_sub = 0
for _ in range(20):
    a,b,c = input().split()
    if c == 'P':
        continue
    if c == 'F':
        score_num += 0
        num_sub += float(b)
        continue
    score_num += float(b) * (4.5 - score.index(c) * 0.5)
    num_sub += float(b)

print(score_num / num_sub)
