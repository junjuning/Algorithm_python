def solution(s, skip, index):
    answer = ''
    arr = 'abcdefghijklmnopqrstuvwxyz'
    arr = list(set(arr) - set(skip))
    arr.sort()
    dic = {arr[i]:i for i in range(len(arr))}
    
    for i in s:
        answer += arr[(dic[i] + index) % len(arr)]
    
    return answer