## 골드2
# LIS 최장 증가 부분 수열

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
# arr= [10, 20, 30, 40, 29, 25, 28, 29, 40]
LIS = [0]

for i in arr:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        left = 0 
        right = len(LIS)
        
        while left < right:
            mid = (left + right) // 2
            if LIS[mid] < i:
                left = mid + 1
            else:
                right = mid
        LIS[right] = i

print(len(LIS)-1)


