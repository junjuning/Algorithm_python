## 골드3
# heapq 사용 -> 힙: 부모자식간 대소 관계 성립
# 우선순위 큐 -> pop하면 작은 값
# 그리디 알고리즘


import sys
import heapq
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    p, d = map(int, sys.stdin.readline().split())
    arr.append([p, d])
    
arr.sort(key = lambda x :x[1])

heap = []
for i in arr:
    heapq.heappush(heap, i[0])
    if(i[1]<len(heap)):
        heapq.heappop(heap)
        
print(sum(heap))
    