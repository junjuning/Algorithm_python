def solution(A,B):
    result1 = 0
    result2 = 0
    
    a1 = sorted(A)
    b1 = sorted(B, reverse = True)
    a2 = sorted(A)
    b2 = sorted(B, reverse = True)
    
    for i in range(len(A)):
        result1 += a1[i] * b1[i]
        result2 += a2[i] * b2[i]
        
    return min(result1, result2)