import sys
n = int(input())

nList = list(map(int, sys.stdin.readline().split()))
m = int(input())
mList = list(map(int, sys.stdin.readline().split()))
nList = sorted(nList)

for i in mList:
    left = 0
    right = n - 1
    flag = 0
    while left <= right:
        mid = (left + right) // 2
        if nList[mid] > i:
            right = mid - 1
        elif nList[mid] < i:
            left = mid + 1
        else:
            flag = 1
            break
    print(flag, end = ' ')