# 큐로 이용해서 풀 수 있는 듯
# 그냥 풀면 풀리는 문제

def solution(priorities, location):
    answer = 0
    while(priorities):
        if(max(priorities) > priorities[0]):
            num = priorities.pop(0)
            priorities.append(num)
        else:
            answer+=1
            if(location == 0):
                return answer
            priorities.pop(0)
            
        if(location != 0):
            location -= 1
        else:
            location = len(priorities) - 1