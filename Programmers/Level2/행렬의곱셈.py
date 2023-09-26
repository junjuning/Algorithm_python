def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        l = arr1[i]
        arr = []
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(l)):
                sum += l[k] * arr2[k][j]
            arr.append(sum)
        answer.append(arr)
    return answer