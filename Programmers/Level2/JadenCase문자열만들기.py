def solution(s):
    answer = []
    answer.append(s[0].upper())
    for i in range(1, len(s)):
        if s[i - 1] == ' ':
            answer.append(s[i].upper())
        else:
            answer.append(s[i].lower())
    return ''.join(answer)