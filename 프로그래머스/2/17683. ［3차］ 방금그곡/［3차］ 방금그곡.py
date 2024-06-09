
def solution(m, musicinfos):
    m = exit_star(m)
    
    musicinfos = [x.split(',') for x in musicinfos]
    new_list = [] # 제목, 재생시간, 악보
    print(musicinfos)

    for music in musicinfos:
        name = music[2] # 제목
        # 재생시간
        start = list(map(int, music[0].split(':')))
        end = list(map(int, music[1].split(':')))
        length = (end[0]-start[0])*60 + end[1]-start[1]
        # 악보
        music_3 = exit_star(music[3])
        paper = music_3 * (length // len(music_3)) + music_3[:length%len(music_3)+1]
        new_list.append([name, length,paper])
    
    answer = []
    for i in range(len(new_list)):
        if m in new_list[i][2]:
            answer.append(new_list[i])
    answer = sorted(answer, key = lambda x : (-x[1]))
    
    if not answer:
        return '(None)'
    else:
        return answer[0][0]
        
# 음에 #이 있다면 소문자로 바꿔줌  
def exit_star(string):
    if '#' not in string:
        return string
    answer = ''
    for i in range(len(string)):
        if string[i] == '#':
            answer = answer[:-1]+answer[-1].lower()
        else:
            answer += string[i]
    return answer
