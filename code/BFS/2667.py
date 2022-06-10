from collections import deque
import sys

n = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
arr = []

for i in range(n):
    arr.append(list(map(int, str(input()))))

q=deque()
def bfs(x, y):
    cnt=1
    arr[x][y]=0
    q.append([x, y])
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=ny<n and 0<=nx<n and arr[nx][ny]==1):
                arr[nx][ny]=0
                q.append([nx, ny])
                cnt+=1
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if(arr[i][j]==1):
            result.append(bfs(i, j))

print(len(result))
result = sorted(result)
for i in result:
    print(i)
