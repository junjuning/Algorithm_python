## 실버2

from collections import deque
import sys

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(soil, a, b):
    q = deque()
    q.append([a, b])
    soil[b][a] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < m and soil[ny][nx] == 1:
                q.append([nx, ny])
                soil[ny][nx] = 0


for _ in range(t):
    count = 0
    m, n, k = map(int, sys.stdin.readline().split())
    soil = [[0] * m for i in range(n)]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        soil[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if soil[i][j] == 1:
                bfs(soil, j, i)
                count += 1
    print(count)
    
            

    

# arr =[[0, 1],[2, 3]]

# print(arr[0][1])