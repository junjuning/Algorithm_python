## 실버2
# combinations()
# 

from itertools import combinations
import sys

n, s = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))

cnt=0
for i in range(1, n+1):
    data = combinations(num, i)
    for j in list(data) :
        if(sum(j)==s) :
            cnt+=1
print(cnt)