
'''
숫자인 문자열 정렬 -> 크기 순으로 정렬이 아니라 앞에서부터 `순서`형식으로 정렬됨
padding은 맨 앞의 숫자를 반복
3 -> 333
31 -> 313131
313 -> 313313313
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, reverse=True, key=lambda x:x*3)
    return str(int("".join(numbers)))