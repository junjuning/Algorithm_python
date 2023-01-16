## 실버 3
# 백트래킹을 잘 설명하는 문제

import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

def dfs():
    if(len(arr) == m):
        print(' '.join(map(str, arr)))
    else:
        for i in range(1, n+1):
            if(i not in arr):
                arr.append(i)
                dfs()
                arr.pop()
    
dfs()