def solution(lottos, win_nums):
    answer = 0   

    result = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    possible = 0
    for i in range(6):
        target = lottos.pop(0)
        if target in win_nums:
            win_nums.remove(target)
            answer += 1
        elif target == 0:
            possible += 1
    
    minResult = answer
    maxResult = answer + possible

    return [result[maxResult], result[minResult]]