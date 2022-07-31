## 골드 5
# DB 배낭문제

import sys

n, t = map(int, sys.stdin.readline().split())
score = [[0,0]]
dp = [[0 for _ in range(t+1)] for _ in range(n+1)]
for _ in range(n): 
    score.append(list(map(int, sys.stdin.readline().split())))


for i in range(1, n+1):
    for j in range(1, t+1):
        if j < score[i][0]:
            dp[i][j] = dp[i-1][j]  
        else: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-score[i][0]] + score[i][1]) 
            
            
print(dp[n][t])