def solution(prices):
    answer = [0, 1]
    num = 1
    minNow = min(prices[len(prices)-2:])
    for i in range(len(prices) - 3, -1, -1):
        num += 1
        if prices[i] > minNow:
            for j in range(i + 1, len(prices)):
                if prices[j] < prices[i]:
                    answer.append(j - i)
                    break
        else:
            answer.append(num)
            minNow = prices[i]
    
    answer.reverse()
    return answer