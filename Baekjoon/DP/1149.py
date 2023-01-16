## 실버 1
# 기본적인 dp지만 3개의 경우를 따로 생각해줘야 함.

import sys
n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1] + arr[i][0], arr[i][0] + arr[i-1][2])
    arr[i][1] = min(arr[i-1][0] + arr[i][1], arr[i][1] + arr[i-1][2])
    arr[i][2] = min(arr[i-1][0] + arr[i][2], arr[i][2] + arr[i-1][1])
    
print(min(arr[n-1][0], arr[n-1][1], arr[n-1][2]))