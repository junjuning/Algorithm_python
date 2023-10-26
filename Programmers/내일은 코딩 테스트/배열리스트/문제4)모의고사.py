def solution(answers):
    score = [0, 0, 0]
    result = []
    n = len(answers)
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(n):
        answer = answers[i]
        if answer == p1[i % 5]:
            score[0] += 1
        if answer == p2[i % 8]:
            score[1] += 1
        if answer == p3[i % 10]:
            score[2] += 1
            
    highest = max(score)
    for i in range(3):
        if score[i] == highest:
            result.append(i + 1)
    return sorted(result)