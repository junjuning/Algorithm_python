from collections import deque
def solution(sticker):
    answer = 0
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    
    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]
        
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])
        
    answer = max(max(dp1), max(dp2))
    return answer