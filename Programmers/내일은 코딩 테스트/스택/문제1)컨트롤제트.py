def solution(s):
    answer = []
    arr = list(s.split(' '))
    
    for i in arr:
        if i == "Z":
            answer.pop()
        else:
            answer.append(int(i))
    return sum(answer)