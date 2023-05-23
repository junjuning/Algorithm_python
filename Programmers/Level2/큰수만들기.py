def solution(number, k):
    answer = []
    totalNum = len(number)-k

    for i in range(totalNum): 
        find = number[:len(number)-totalNum+1+i]
        if "9" in find:
            number = number[number.index("9") + 1:]
            answer.append("9")
            continue
        maxNum = max(find)
        number = number[number.index(maxNum)+1:]
        answer.append(maxNum)
        
    return "".join(answer)