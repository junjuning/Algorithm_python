import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
left = 0
right = n - 1

print(arr)
result = 10000000000
resultL = 0
resultR = n - 1
while left < right:
    sum = arr[left] + arr[right]
    print(arr[left], arr[right])
    print(sum)
    if abs(sum) < abs(result):
        resultL = arr[left]
        resultR = arr[right]
        result = sum
    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        break


print(resultL, resultR)