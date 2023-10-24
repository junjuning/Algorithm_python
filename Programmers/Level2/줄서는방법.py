import math

def solution(n, k):
    answer = []
    check = [i for i in range(1, n + 1)]
    
    while check:
        now = (k - 1) // math.factorial(n - 1)
        answer.append(check.pop(now))
        k = k % math.factorial(n - 1)
        n -= 1
    return answer