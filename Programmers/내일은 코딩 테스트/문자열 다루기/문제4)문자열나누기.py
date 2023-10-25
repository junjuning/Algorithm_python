def solution(s):
    answer = 0
    
    a, b = 0, 0
    key = s[0]
    for i in range(len(s)):
        if a == b:
            answer += 1
            key = s[i]
        if key == s[i]:
            a += 1
        else:
            b += 1
    return answer