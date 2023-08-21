## 골드2
# LIS
# 가장 긴 증가하는 부분 수열2와의 차이점은, 음수가 들어갈 수 있어서 LIS 배열 생성 초기 0을 넣어주면 안된다는 점

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

result = [arr[0]]

for i in range(1, n):
    if result[-1] < arr[i]:
        result.append(arr[i])
    else:
        left = 0
        right = len(result) - 1
        
        while left < right:
            mid = (left + right) // 2
            if arr[i] > result[mid]:
                left = mid + 1
            else:
                right = mid
        result[right] = arr[i]

print(len(result))