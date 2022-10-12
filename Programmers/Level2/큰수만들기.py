def solution(number, k):
    answer = []
    totalNum = len(number)-k

    for i in range(totalNum): 
        maxNum = max(number[:len(number)-totalNum+1+i])
        number = number[number.index(maxNum)+1:]
        answer.append(maxNum)

    return "".join(answer)
    