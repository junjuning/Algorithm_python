import sys
t = int(input())

for i in range(t):
    arr = []
    n, m = map(int, sys.stdin.readline().split())
    for i in range(m):
        arr.append(list(map(int, sys.stdin.readline().split())))
    print(n-1)