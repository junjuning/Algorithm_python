## 최대힙. 
# 그냥 힙은 최소힙이지만 -1을 이용해서 최대힙 구현

import heapq
def solution(n, works):
    answer = 0
    arr = []
    heapq.heapify(arr)
        
    for i in works:
        heapq.heappush(arr, -i)
        
    for i in range(n):
        a = heapq.heappop(arr)
        if a == 0:
            break
        heapq.heappush(arr, -(a * -1 - 1))

    for i in arr:
        answer += i * i
    return answer