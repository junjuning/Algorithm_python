def solution(n, left, right):
    arr = []

    for i in range(left, right + 1):
        v = max(i//n, i%n) + 1 
        arr.append(v)
        
    return arr