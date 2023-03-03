def solution(A,B):
    result = 0
    
    A.sort()
    B.sort(reverse = True)

    for i in range(len(A)):
        result += A[i] * B[i]
    
    return result