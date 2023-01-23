import sys
sys.setrecursionlimit(10**9)
n = int(input())

arr = [[] for _ in range(n + 1)]

par = [0 for i in range(n + 1)]

for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)


def dfs(n):
    for i in arr[n]:
        if(par[i] == 0):
            par[i] = n
            dfs(i)

dfs(1)

for i in range(2, n + 1):
    print(par[i])