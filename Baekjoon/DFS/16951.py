## 실버2

from collections import deque
import sys
sys.setrecursionlimit(10**9)

a, b = map(int, sys.stdin.readline().split())

arr = deque()
arr.append([a, 1])

# def dfs():
#     now, cnt = arr.popleft()
#     a1 = now * 2
#     a2 = int(str(now) + '1')

#     if(a1 == b or a2 == b):
#         print(cnt + 1)
#         return

#     if(a1 < b):
#         arr.append([a1, cnt + 1])
#     if(a2 < b):
#         arr.append([a2, cnt + 1])
        
#     if(len(arr) == 0):
#         print(-1)
#         return 
#     dfs()
    
# dfs()

def dfs():
    while(arr):
        now, cnt = arr.popleft()
        a1 = now * 2
        a2 = int(str(now) + '1')

        if(a1 == b or a2 == b):
            print(cnt + 1)
            return

        if(a1 < b):
            arr.append([a1, cnt + 1])
        if(a2 < b):
            arr.append([a2, cnt + 1])
            
    print(-1)
    
dfs()



