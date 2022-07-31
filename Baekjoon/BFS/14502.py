from collections import deque
from itertools import combinations
import sys

n, m = map(int, input().split())
arr=[]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
q=deque()
def bfs():
    while(q):
        q.popleft()


for i in arr:
    for j in i :
        
# print(list(combinations([i for i in range(n*m)], 3)))

# print(wall)
# print([i for i in range(n*m)])