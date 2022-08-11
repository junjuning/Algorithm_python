# 스택/큐
# 데큐 최고
# 리스트[-1]은 마지막을 가르킴

from collections import deque

def solution(progresses, speeds):
    q = deque()
    answer = []
    for i in range(len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        if((100 - progresses[i]) % speeds[i] != 0):
            day+=1
        q.append(day)
    
    num = 0
    for i in q:
        if(i > num):
            answer.append(1)
            num = i
            
        else:
            answer[-1] += 1
    return answer
