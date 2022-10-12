## 실버 5

import sys
n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))
    
arr.sort()
print('\n'.join(map(str, arr)))