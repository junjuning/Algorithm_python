## 실버3
# dp + Bruth Force

import sys

n = int(input())
arr = []
dp = [] 
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    dp.append(0)
dp.append(0)
for i in range(n-1, -1, -1):
    t = arr[i][0]
    p = arr[i][1]
    
    if(t + i <= n):
        dp[i] = max(dp[i+1], p+dp[i+t])
        
    else:
        dp[i] = dp[i+1]
        
print(dp[0])