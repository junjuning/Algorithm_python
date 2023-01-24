## 실버 1

import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, n, k = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(n)] for _ in range(m)]
cnt = 1

for _ in range(k):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            arr[i][j] = 1

cntArr = []

def dfs(x, y):
    global cnt
    arr[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[ny][nx] == 0:
                cnt += 1
                dfs(nx, ny)

for y in range(m):
    for x in range(n):
        if arr[y][x] == 0:
            dfs(x, y)
            cntArr.append(cnt)
            cnt = 1

print(len(cntArr))
print(' '.join(map(str, sorted(cntArr))))