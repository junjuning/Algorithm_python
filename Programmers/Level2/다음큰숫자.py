def solution(n):
    answer = n + 1
    
    while True:
        if str(bin(answer)).count('1') == str(bin(n)).count('1'):
            break
        answer += 1
    return answer