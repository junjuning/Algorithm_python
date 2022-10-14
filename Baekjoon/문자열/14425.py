## 실버 3

import sys
n, m = map(int, sys.stdin.readline().split())


s = list(sys.stdin.readline().strip() for _ in range(n))
arr = list(sys.stdin.readline().strip() for _ in range(m))

cnt = 0
for i in arr:
    if(i in s):
        cnt += 1
        
print(cnt)