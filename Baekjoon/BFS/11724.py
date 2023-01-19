## 실버2
# 그래프 + bfs

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n+1)]for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
visit[0] = 1
q = deque()
count = 0

def bfs(v):
    q.append(v)
    while(q):
        v = q.popleft()
        for i in range(1, n+1):
            if(graph[i][v]==1 and visit[i] == 0):
                visit[i] = 1
                q.append(i)
                


for i in range(m):
    x, y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1, n+1):
    if(visit[i] == 0):
        bfs(i)
        count += 1
        
print(count)