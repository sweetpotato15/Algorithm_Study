import sys
input = sys.stdin.readline

def tictacto(string):
    # X의 개수 - O의 개수 = 0,1 이 아니면 불가능
    count = string.count('X') - string.count('O')
    if count < 0 or  count > 1: return 'invalid'

    # 가로, 세로, 대각선 가능한 경우
    valid = [string[:3], string[3:6], string[6:]]
    valid += [string[0]+string[3]+string[6], string[1]+string[4]+string[7],string[2]+string[5]+string[8], string[0]+string[4]+string[8],string[2]+string[4]+string[6]]

    O = valid.count('OOO')
    X = valid.count('XXX')

    # x 와 o의 개수가 같을 때 (보드판을 채우지 않고도 끝낼 수 있는 경우 = o가 승리) 
    # -> xxx 는 없고 ,ooo 있을 때만 valid
    if count == 0 :
        if O == 1 and X == 0: return 'valid' 
        else: return 'invalid'
    
    # x 개수 = o 개수 - 1 (보드판을 모두 채운 경우/ 안채운 경우 = x가 승리 or 승리자 없음)
    else:
        if string.count('.') == 0: # 모두 채운 경우 (둘다 완성 못함 or 마지막에 x가 완성)
            if O == 0: return 'valid'
            else: return 'invalid'
        else: # 모두 안채운 경우 = x가 승리
            if X == 1 and O == 0 : return 'valid'
            else: return 'invalid'

while True:
    word = input().strip()
    if word == 'end':
        break
    answer = tictacto(word)
    print(answer)