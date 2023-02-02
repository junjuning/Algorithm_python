## 실버2

from collections import deque
import sys
sys.setrecursionlimit(99999)

num = []
result = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = deque()
for _ in range(5):
    num.append(list(map(str, sys.stdin.readline().split())))
    
def bfs(x, y, now):
    if(len(now) == 6):
        if(now not in result):
            result.append(now)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if(0 <= nx < 5 and 0 <= ny < 5):
            bfs(nx, ny, now + num[ny][nx])
            

for i in range(5):
    for j in range(5):
        bfs(j, i, str(num[i][j]))

print(len(result))