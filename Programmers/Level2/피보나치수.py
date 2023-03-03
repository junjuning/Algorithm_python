def solution(n):
    answer = 0
    f = [0, 1, 1, 2]
    
    if n >= 4:
        for i in range(4, n + 1):
            f.append(f[i-1] + f[i-2])

    return f[n] % 1234567