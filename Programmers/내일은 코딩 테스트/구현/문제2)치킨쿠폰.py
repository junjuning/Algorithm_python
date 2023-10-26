def solution(chicken):
    answer = 0
    while chicken >= 10:
        n = chicken // 10
        chicken -= n * 10
        chicken += n
        answer += n
    return answer