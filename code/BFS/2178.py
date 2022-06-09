## 실버1
# 기본 bfs, bfs를 이해하기 가장 좋은 예제

from collections import deque

n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
arr = []
for i in range(n) :
    arr.append(list(map(int, str(input()))))
    
def bfs(x, y):
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<m and arr[nx][ny]==1):
                arr[nx][ny]=arr[x][y]+1
                q.append([nx, ny])
    return arr[n-1][m-1]

print(bfs(0,0))