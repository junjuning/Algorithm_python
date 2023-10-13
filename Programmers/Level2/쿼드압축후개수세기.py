def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def check(x, y, n):
        key = arr[y][x]
        for i in range(y, y + n):
            for j in range(x, x + n):
                if arr[i][j] != key:
                    check(x, y, n // 2)
                    check(x + n // 2, y, n // 2)
                    check(x, y + n // 2, n // 2)
                    check(x + n // 2, y + n // 2, n // 2)
                    return 
        answer[key] += 1
    check(0, 0, n)
    return answer