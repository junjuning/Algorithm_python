## 실버1

from collections import deque
import sys

dx = [-1, 0, 1, 0, 0]
dy = [0, -1, 0, 1, 0]

r, c = map(int, sys.stdin.readline().split())
arr = []
q = deque()
visit = [[0 for _ in range(c)] for _ in range(r)]
for _ in range(r):
    arr.append(sys.stdin.readline())
    
def bfs(x, y):
    global ts, tw
    q.append([x, y])
    wolf, sheep = 0, 0
    while q:
        x, y = q.popleft()
        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<c and 0<=ny<r and arr[ny][nx] != '#' and visit[ny][nx] == 0):
                if(arr[ny][nx] == 'v'):
                    wolf += 1
                if(arr[ny][nx] == 'o'):
                    sheep += 1
                q.append([nx, ny])
                visit[ny][nx] = 1
    if wolf >= sheep:
        tw += wolf
    else:
        ts += sheep



ts = 0 
tw = 0


for i in range(r):
    for j in range(c):
        if(arr[i][j] == 'v' or arr[i][j] == 'o' and visit[i][j] == 0):
            bfs(j, i)


print(ts, tw)