import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())

low, high = 0, max(arr)

while low <= high:
    sum = 0
    mid = (low + high) // 2
    for i in arr:
        if i <= mid:
            sum += i
        else: 
            sum += mid
    if sum <= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)