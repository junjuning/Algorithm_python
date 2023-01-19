## 실버 2

import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0] = arr[0]

if(n >= 2):
    for i in range(1, n):
        dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))