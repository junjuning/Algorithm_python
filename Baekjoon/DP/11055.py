## 실버2

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
        else:
            dp[i] = max(arr[i], dp[i])

print(max(dp))