import sys
from math import ceil
input = sys.stdin.readline
n = int(input()) # 스위치 개수
switch = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    sex, index = map(int, input().split())
    if sex == 1: # 남자라면
        for i in range(1,n//index+1):
            switch[index* i-1] = 1 - switch[index*i-1]
    elif sex == 2 : # 여자라면
        switch[index-1] = 1-switch[index-1]
        left , right = index-2, index
        while left >= 0 and right <= n-1 and switch[left] == switch[right]:
            switch[left] = 1 - switch[left]
            switch[right] = 1 - switch[right]
            left -= 1
            right += 1

for i in range(0,len(switch),20):
    print(*switch[i:i+20])