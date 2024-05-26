# 

def solution(dartResult):
    dartResult = dartResult.replace('10','?')
    array = list(dartResult)

    number = []
    for i in range(len(array)):
        # print(number)
        if array[i] == '?':
            number.append(10)
        elif array[i].isdigit():
            number.append(int(array[i]))
            
        elif array[i] == 'D':
            number.append((number.pop())**2)
        elif array[i] == 'T':
            number.append((number.pop())**3)
        elif array[i] == '*':
            if len(number) >= 2:
                second = number.pop()
                first = number.pop()
                number.append(first*2)
                number.append(second*2)
            elif len(number) == 1:
                number.append(number.pop() * 2)
        elif array[i] == '#':
            number.append(-number.pop())
        
    answer = sum(number)
    return answer
    # option = ['*','#']
    # score = ['S','D','T']
    # for i in range(len(dartResult)):
    #     if array[i] in option or array[i] in score:
            



    