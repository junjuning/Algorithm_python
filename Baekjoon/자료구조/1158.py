## 실버4
# deque 사용
# 양방향 큐 O(1)

import sys
from collections import deque

n, k=map(int, sys.stdin.readline().split())
que=deque(range(1, n+1))

list=[]
while len(que)>=1 :
    que.rotate(-(k-1))
    list.append(que.popleft())
 
     
print('<'+", ".join(map(str, list))+'>')