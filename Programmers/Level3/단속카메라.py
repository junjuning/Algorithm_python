# 그리디
def solution(routes):
    answer = -30000
    cnt = 0
    routes.sort(key = lambda x: x[1])
    
    for i, j in routes:
        if i > answer:
            cnt += 1
            answer = j
    return cnt