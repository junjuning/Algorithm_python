## 골드4

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]
result = []

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

num = max(dp)
print(num)
result = []
for i in range(n - 1, -1, -1):
    if dp[i] == num:
        result.append(arr[i])
        num -= 1
        
result.reverse()
for i in result:
    print(i, end = " ")