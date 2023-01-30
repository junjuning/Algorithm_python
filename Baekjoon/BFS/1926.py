from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = deque()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


area = 0
pic = []
def bfs(x, y):
    q.append([x, y])
    arr[y][x] = 0
    cnt = 1
    while(q):
        nx, ny = q.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            
            if(0 <= x < m and 0 <= y < n):
                if arr[y][x] != 0:
                    arr[y][x] = 0
                    cnt += 1
                    q.append([x, y])
    return cnt
  

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(arr[i][j] != 0):
            pic.append(bfs(j, i))

print(len(pic))
if(len(pic) == 0):
    print(0)
else:
    print(max(pic))