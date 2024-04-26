import sys
input = sys.stdin.readline

n, game = input().split()
names = [input() for _ in range(int(n))]
names = list(set(names))
games = ["Y","F","O"]
for i in range(3):
    if games[i] == game:
        answer = len(names) // (i+1)
print(answer)