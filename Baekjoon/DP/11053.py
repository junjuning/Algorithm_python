## 실버2
# 가장 긴 증가하는 부분수열
# dp와 이분탐색으로 푸는 방법이 있음. 이분탐색은 빠르지만 부분 수열을 정확하게 알 수 없음. 개수만 알 수 있음.

import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))


## 1. 이분 탐색 풀이
# result = [arr[0]]

# for i in range(1, n):
#     if arr[i] > result[-1]:
#         result.append(arr[i])
#     else:
#         left = 0
#         right = len(result) - 1
#         while left < right:
#             mid = (left + right) // 2
            
#             if result[mid] < arr[i]:
#                 left = mid + 1
#             else:
#                 right = mid
#         result[right] = arr[i]

# print(len(result))

## 2. dp
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))