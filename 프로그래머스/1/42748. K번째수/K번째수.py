def solution(array, commands):
    answer = []
    for i in commands:
        my_array = array[i[0]-1:i[1]]
        my_array.sort()
        answer.append(my_array[i[2]-1])

    return answer