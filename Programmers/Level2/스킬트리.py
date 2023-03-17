def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        s = ''
        for j in i:
            if j in skill:
                s += j
        if s == skill[:len(s)]:
            answer += 1
        
    return answer