## 실버3
# deque
import sys
from collections import deque

dq = deque()
n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
list.reverse()

for i in range(n):
   if(list[i]==1):
      dq.appendleft(i+1)
   elif(list[i]==2):
      dq.insert(1, i+1)
   else:
      dq.append(i+1)
      
   
for i in dq:
    print(i, end = ' ')