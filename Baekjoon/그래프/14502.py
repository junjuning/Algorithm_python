import sys
import copy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = 0

def bfs():
    q = deque()
    graph = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append([i, j])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                q.append([ny, nx])
    cnt = 0
    for i in range(n):
        cnt += graph[i].count(0)
    
    global answer
    answer = max(answer, cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0
                
wall(0)
print(answer)