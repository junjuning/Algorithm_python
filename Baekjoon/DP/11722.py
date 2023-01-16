## 실버 2

import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
num = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if(arr[j] > arr[i]):
            num[i] = max(num[i], num[j]+1)
    

print(max(num))