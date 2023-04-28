def solution(n, s):
    if n > s:
        return [-1]
    num = s//n
    answer = [num] * n
    for i in range(s-num*n):
        answer[i] += 1
    return sorted(answer)