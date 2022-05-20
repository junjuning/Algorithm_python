## 골드 4
# 파라메트릭 이분탐색

import sys

n, m, l = map(int, sys.stdin.readline().split())
rest = list(map(int, sys.stdin.readline().split()))

start = 1
rest.append(l)
rest.append(0)
end = l
dist = []
rest.sort()
for i in range(len(rest)-1):
    dist.append(rest[i+1]-rest[i])
 
while(start<=end):
    mid = (start+end)//2 # 휴게소 간 거리
    cnt=0
    for i in dist:
        if(i>mid):
            cnt += (i - 1)//mid

    if(cnt<=m):
        end = mid -1
        result = mid
    else:
        start = mid + 1
    
print(result)
        
# 거리를 이분탐색
# mid 보다 간격이 넓으면 들어가야하는 개수 그 개수가 m보다 많으면 mid를 늘려야 함