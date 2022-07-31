## 실버2
# 기본 dfs 문제
# RecursionError 해결 -> sys.setrecursionlimit(5000)
# 처음맞는 재귀 에러..이러면 bfs로 풀어야되나

import sys
sys.setrecursionlimit(5000)

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]

def dfs(y, x):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<w and 0<=ny<h and arr[ny][nx]==1):
            arr[ny][nx]=0
            dfs(ny, nx)
    

while(True):
    cnt = 0
    w, h =map(int, input().split())
    if(w==0 and h==0):
        break
    arr = []
    for i in range(h) :
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(h):
        for j in range(w):
            if(arr[i][j]==1):
                dfs(i, j)
                cnt+=1
    print(cnt)
        
    