from collections import deque
import sys

n = int(input())
arr = [list(input()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
cnt = 0
q = deque()

def bfs(x,y):
    q.append([x,y])
    visited[x][y]=1
    while q:
        x, y = q.popleft()
        for i, j in [[1,0],[-1,0],[0,1],[0,-1]]:
            xx = x + i
            yy = y + j
            if(0<=xx<n and 0<=yy<n):
                if(arr[xx][yy]==arr[x][y] and visited[xx][yy]==0):
                    q.append([xx,yy])
                    visited[xx][yy] = 1
            
for i in range(n) :
    for j in range(n) :
        if(visited[i][j]==0):
            bfs(i,j)
            cnt+=1
            
print(cnt, end =' ')
visited = [[0] * n for _ in range(n)]
cnt = 0

for i in range(n) :
    for j in range(n) :
        if(arr[i][j]=='R'):
            arr[i][j]='G'
            
for i in range(n) :
    for j in range(n) :
        if(visited[i][j]==0):
            bfs(i,j)
            cnt+=1
            
print(cnt)
# 돌아다니면서, 방문 안했고 같은 색이면 방문, 

