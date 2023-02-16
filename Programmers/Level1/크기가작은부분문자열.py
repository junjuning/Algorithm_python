def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        n = t[i:i + len(p)]
        if n <= p:
            answer += 1

    return answer