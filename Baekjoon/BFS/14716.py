from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
arr = []
dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]
q = deque()
num = 0

for _ in range(m):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
def bfs(x, y):
    q.append([x, y])
    arr[y][x] = 1
    while(q):
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<m):
                if(arr[ny][nx] == 1):
                    arr[ny][nx] = 0
                    q.append([nx, ny])
    

for i in range(m):
    for j in range(n):
        if(arr[i][j] == 1):
            bfs(j, i)
            num += 1
            
print(num)