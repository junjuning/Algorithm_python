def solution(n):
    arr = [0, 1, 2, 3]
    
    if n >= 4:
        for i in range(4, n + 1):
            arr.append(arr[i - 1] + arr[i - 2])
            
    return arr[n] % 1234567