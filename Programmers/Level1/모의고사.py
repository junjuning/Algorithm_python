def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    score = [0, 0, 0]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        index1 = i % 5
        index2 = i % 8
        index3 = i % 10
        now = answers[i]

        if(first[index1]==now):
            score[0] += 1
        if(second[index2]==now):
            score[1] += 1
        if(third[index3]==now):
            score[2] += 1
            
    maxScore = max(score)
    for i in range(3):
        if (score[i] == maxScore):
            answer.append(i+1)
    return answer
