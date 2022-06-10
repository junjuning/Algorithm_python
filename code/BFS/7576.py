from collections import deque
import sys

m, n = map(int, input().split(' '))

arr=[]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q=deque()

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if arr[i][j]==1:
            q.append([i, j])

def bfs():
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<m and arr[nx][ny]==0):
                q.append([nx, ny])
                arr[nx][ny] = arr[x][y]+1
                
bfs()
result = 0
for i in arr:
    for j in i :
        if(j==0):
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result-1)
            


#가장 빨리 다 다녀오는 횟수 -1??