import sys
input = sys.stdin.readline

p, m = map(int, input().split())
player = []
for i in range(p):
    a,b = input().split()
    a = int(a)
    player.append([a,b])

group = [] # 각 그룹
start = [] # 각 그룹의 첫 플레이어의 레벨

x = player.pop(0)
group.append([x]) # [[[10,'a]]]
start.append(x[0]) # 10

while player:
    new = player.pop(0)
    level = new[0]
    id = new[1]

    for i in range(len(group) ):
        if start[i] - 10 <= level <= start[i] + 10 and len(group[i]) < m:
            group[i].append(new)
            break
        
        if len(group[i]) == m:
            continue
    else:
        group.append([new])
        start.append(level)
        
for i in range(len(group)):
    answer = sorted(group[i], key = lambda x : x[1])
    if len(group[i]) == m:
        print('Started!')
    else:
        print('Waiting!')

    for i in answer:
        print(*i)