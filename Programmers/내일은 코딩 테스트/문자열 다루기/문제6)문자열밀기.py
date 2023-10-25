def solution(A, B):
    for i in range(len(B)):
        if A == B: 
            return i 
        A = A[-1] + A[:-1]

    return -1
