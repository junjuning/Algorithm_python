import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

low = 1
high = max(arr)

while low <= high:
    sum = 0
    mid = (low + high) // 2
    for i in arr:
        if i > mid:
            sum += (i - mid)

    if sum < m:
        high = mid -1
    else:
        low = mid + 1

print(high)