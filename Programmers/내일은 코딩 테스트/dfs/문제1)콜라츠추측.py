def solution(num):
    
    def cur(n, answer):
        if answer >= 500:
            return -1
        if n == 1:
            return answer
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        return cur(n, answer + 1)
        
    answer = cur(num, 0)
    return answer