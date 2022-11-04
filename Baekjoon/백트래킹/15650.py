## 실버3

import sys

n, m = map(int, sys.stdin.readline().split())

arr = []

def dfs(s):
    if(len(arr)==m):
        print(' '.join(map(str, arr)))
    
    for i in range(s, n+1):
        if(i not in arr):
            arr.append(i)
            dfs(i)
            arr.pop()

dfs(1)