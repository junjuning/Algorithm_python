## 플로이셜 워셜 알고리즘
# 모든 정점에서의 다른 모든 지점까지의 최단거리 구하는 경우

import sys

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 or (arr[i][k] == 1 and arr[k][j] == 1):
                arr[i][j] = 1
                

for i in arr:
    for j in i:
        print(j, end = ' ')
    print()