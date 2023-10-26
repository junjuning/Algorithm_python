def solution(order):
    answer = 0
    arr = ["3", "6", "9"]
    order = str(order)
    for i in order:
        if i in arr:
            answer += 1
    return answer