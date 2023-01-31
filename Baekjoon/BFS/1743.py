## 실버 1

from collections import deque
import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
visit =[[0] for _ in range(m) for _ in range(n)]

q = deque()


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    arr[r][c] = 1

answer = []
def bfs(x, y):
    q.append([x, y])
    arr[y][x] = -1
    result = 1
    while(q):
        c, r = q.popleft()
        for i in range(4):
            ny = r + dy[i]
            nx = c + dx[i]
            
            if(0 < nx <= m and 0 < ny <= n and arr[ny][nx] == 1):
                result += 1
                arr[ny][nx]= -1
                q.append([nx, ny])
    return result

for i in range(1, n+1):
    for j in range(1, m+1):
        if(arr[i][j]==1):
            answer.append(bfs(j, i))
print(max(answer))