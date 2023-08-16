import sys
n, k = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(input()))

left = 1
right = max(arr)
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    
    for i in arr:
        cnt += i // mid
    
    if cnt < k:
        right = mid - 1
    elif cnt >= k:
        left = mid + 1
print(right)
    
