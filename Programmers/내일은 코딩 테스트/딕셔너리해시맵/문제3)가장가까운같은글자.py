def solution(s):
    answer = []
    dict = {}
    
    for i in range(len(s)):
        c = s[i]
        if c not in dict:
            answer.append(-1)
        else:
            answer.append(i - dict[c])
        dict[c] = i
    return answer