# heap. 자동으로 정렬해 줌.
# 파이썬 진짜 편하다..힙 구현하기..
# 마지막 예외처리만 쫌 더 신중하게!

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(scoville[0]<K):
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        result = a + b*2
        heapq.heappush(scoville, result)
        answer+=1
        
        if(len(scoville)==1 and scoville[0]<K):
            return -1
    return answer