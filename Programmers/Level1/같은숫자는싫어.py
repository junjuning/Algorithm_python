def solution(arr):
    answer = []
    num = arr[0]
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if(num != arr[i]):
            answer.append(arr[i])
            num = arr[i]

    return answer