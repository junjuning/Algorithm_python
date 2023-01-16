## 실버3

import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
def dfs(num):
    if(len(arr) == m):
        print(' '.join(map(str, arr)))
    
    else:
        for i in range(num, n + 1):
            arr.append(i)
            dfs(i)
            arr.pop()
            
dfs(1)