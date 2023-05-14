def solution(n, stations, w):
    answer = 0
    num = 2 * w + 1
    left = 1
    stations.append(n + w + 1)
    
    for station in stations:
        right = station - w
        answer += (right - left) // num
        if (right - left) % num != 0:
            answer += 1
        left = station + w + 1

    return answer