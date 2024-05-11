import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
t = int(input())
def Note(n2,note1, note2):
    note1 = list(set(note1))
    note1.sort()
    for i in note2:
        index = bisect_right(note1, i) - bisect_left(note1, i)
        if index == 1:
            print(1)
        else:
            print(0)
    
for i in range(t):
    n1 = int(input())
    note1 = list(map(int, input().split()))
    n2 = int(input())
    note2 = list(map(int, input().split()))
    Note(n2, note1, note2)
    