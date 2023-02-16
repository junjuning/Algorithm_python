from collections import deque
import sys

a, b, c = map(int, sys.stdin.readline().split())

q = deque()
visit = [0 for _ in range(201)]

def bfs(x, y, z):
    q.append([x, y, z])
    while q:
        n = q.popleft()
        for i in range():
            
bfs(0, 0, 10)
q.sort()

print(' '.join(map(str, q)))