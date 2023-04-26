def solution(triangle):
    answer = 0
    arr = triangle
    
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            arr[i][j] += max(arr[i + 1][j], arr[i + 1][j + 1])

    return arr[0][0]