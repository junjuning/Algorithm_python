## 골드 5
# 문자열 문제지만 DP로 풀었더니 시간 초과남.

import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

dp = [[0 for _ in range(len(second)+1)] for _ in range(len(first))]
result = 0
 
for i in range(len(first)):
    for j in range(len(second)):
        if(first[i] == second[j]):
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(result, dp[i][j])
print(result)

# import sys
# input = sys.stdin.readline
# first = str(input().strip())
# second = str(input().strip())

# if(len(first)>len(second)):
#     first, second = second, first
# start = 0
# end = 1
# answer = 0 
# while start<=end and end<=len(first):
#     if(first[start:end] in second):
#         answer = max(len(first[start:end]), answer)
#         end += 1
#     else:
#         start +=1
#         end += 1
# print(answer)

