## 실버2

import sys
sys.setrecursionlimit(100000)

n = int(input())
p1, p2 = map(int, sys.stdin.readline().split())
m = int(input())

tree = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]


for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    tree[y].append(x)
    tree[x].append(y)

def dfs(x):
    for i in tree[x]:
        if(visit[i] == 0):
            visit[i] = visit[x] + 1
            dfs(i)
        

dfs(p1)
if visit[p2]>0:
    print(visit[p2])
else:
    print(-1)