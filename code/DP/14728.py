import sys

n, W = map(int, input().split())
list = [[0,0]]
dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

for _ in range(n):
    list.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for w in range(1, W + 1):
        if w >= list[i][0]:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-list[i][0]] + list[i][1]) 
        else: 
            dp[i][w] = dp[i-1][w]

print(dp[n][W])