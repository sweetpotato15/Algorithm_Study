t = int(input())
def room(h,w,n):


    floor = n % h # 몇 층인지 0 ~ h-1 
    if floor == 0:
        floor = h

  # 몇번 방인지 
    if n % h == 0:
        r = n // h
    else:
        r = n // h+1


    # 실제 출력 부분
    if r < 10:
        print("{}0{}".format(floor, r))
    else:
        print("{}{}".format(floor, r))



for i in range(t):
    h,w,n = map(int, input().split())
    room(h,w,n)