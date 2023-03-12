def solution(msg):
    answer = []
    arr = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    i = 0
    str = []
    while i < len(msg) - 1:
        for j in range(i, len(msg)):
            str.append(msg[j])
            if ''.join(str) not in arr:

                arr.append(''.join(str))
                answer.append(arr.index(''.join(str[0:len(str) - 1])))
                str = []
                break
        i = j
    
    if str:
        if ''.join(str) in arr:
            answer.append(arr.index(''.join(str[0:len(str)])))
        else:
            answer.append(len(arr))
    else:
        answer.append(arr.index(msg[-1]))
                  
    return answer