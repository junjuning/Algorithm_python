## 실버 2
# bfs와 dfs

from collections import deque
import sys
n, m, v = map(int, sys.stdin.readline().split())

q = deque()

arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x][y] = 1
    arr[y][x] = 1
    
def bfs(x):
    q.append(x)
    visit[x] = 1
    while(q):
        now = q.popleft()
        print(now, end = ' ')
        for i in range(1, n+1):
            if(arr[now][i] == 1 and visit[i] == 0):
                q.append(i)
                visit[i] = 1



def dfs(x):
    visit[x] = 1
    print(x, end = ' ')
    for i in range(1, n+1):
        if arr[x][i] == 1 and visit[i] == 0:
            dfs(i)


dfs(v)
print()
visit = [0 for _ in range(n+1)]
bfs(v)