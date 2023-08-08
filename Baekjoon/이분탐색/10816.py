import sys
from collections import Counter
n = int(input())
nList = list(map(int, sys.stdin.readline().split()))

m = int(input())
mList = list(map(int, sys.stdin.readline().split()))

nList = sorted(nList)
count = Counter(nList)

for i in mList:
    flag = 0
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nList[mid] < i:
            left = mid + 1
        elif nList[mid] > i:
            right = mid - 1
        elif nList[mid] == i:
            flag = count[i]
            break
    print(flag, end = ' ')
            