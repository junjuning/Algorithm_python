## 골드 1
# heapq쓰면 너무 간단한 문제

import heapq
import sys
n = int(sys.stdin.readline())

sum = 0
arr = []
for i in range(n):
    heapq.heappush(arr, int(sys.stdin.readline()))


while len(arr)>=2:
    now = heapq.heappop(arr)+heapq.heappop(arr)
    sum += now
    heapq.heappush(arr, now)
    
print(sum)