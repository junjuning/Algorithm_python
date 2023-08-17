import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
left = 0
right = n - 1
resultLeft = 0
resultRight = n - 1
result = 10000000000
while left < right :
    mid = arr[left] + arr[right]
    if mid == 0:
        resultLeft = left
        resultRight = right
        break
    if abs(mid) < abs(result):
        result = mid
        resultLeft = left
        resultRight = right
    if mid < 0:
        left += 1
    else:
        right -= 1

print(arr[resultLeft], arr[resultRight])