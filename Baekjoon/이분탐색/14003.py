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