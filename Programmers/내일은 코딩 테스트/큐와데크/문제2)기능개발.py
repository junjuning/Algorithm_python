def solution(progresses, speeds):
    answer = []
    deploy = -1
    num = 0
    for i in range(len(progresses)):
        day = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
        if deploy == -1:
            deploy = day
            num += 1
        else:
            if deploy >= day:
                num += 1
            else:
                answer.append(num)
                num = 1
                deploy = day
    answer.append(num)
    return answer