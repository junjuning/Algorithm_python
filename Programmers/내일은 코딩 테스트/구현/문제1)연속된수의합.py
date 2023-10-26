def solution(num, total):
    answer = []
    avg = total // num
    for i in range(avg - (num - 1) // 2, avg + num // 2 + 1):
        answer.append(i)
    return answer