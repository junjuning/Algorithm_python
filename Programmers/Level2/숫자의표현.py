def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        arr = []
        for j in range(i, n + 1):
            arr.append(j)
            if sum(arr) == n:
                answer += 1
                break
            if sum(arr) > n:
                break
            
    return answer