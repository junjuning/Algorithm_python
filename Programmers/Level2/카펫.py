# 완전탐색

def solution(brown, yellow):
    answer = []
    n = brown // 2 + 2
    
    for y in range(1, n-1):
        x = n - y
        if (x-2) * (y-2) == yellow:
            return [x, y]