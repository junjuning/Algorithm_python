## 실버1
# 우선순위큐로 구현했을 때는 시간초과
# heapq를 사용하자!

import heapq
import sys
n = int(input())

q = []

for i in range(n):
    now = int(sys.stdin.readline().rstrip())
    if(now == 0):
        if(not q):
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(now), now))
        
        
## 실패코드

# import queue
# import sys
# n = int(input())

# q = queue.PriorityQueue()

# for i in range(n):
#     now = int(sys.stdin.readline().rstrip())
#     if(now == 0):
#         if(not q):
#             print(0)
#         else:
#             print(q.get()[1])
#     else:
#         q.put((abs(now), now))