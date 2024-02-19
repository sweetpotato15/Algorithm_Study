n = int(input()) # 지불할 돈 
money = 1000 - n # 거슬러줘야할 돈

money_list = [500,100,50,10,5,1] # 잔돈 단위
count = 0

while money > 0 :
    for i in money_list:

        if money // i > 0 : # 몫이 0보다 클때
            count += money // i
            money = money % i # 남은 금액 조정
            

print(count) 