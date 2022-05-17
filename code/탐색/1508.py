## 골드2
# 파라메트릭 서치
# 이진탐색

import sys
n, m, k = map(int, input().split())

place=list(map(int, sys.stdin.readline().split()))

start = 0
end = n
fin = 0
while(start <= end) :
    mid = (start+end)//2
    pre = 0 # 직전 심판 위치
    num = 1 #심판 수
    str = "1"
    for i in range(1, k):
        if(place[i]-place[pre] >= mid):
            str+="1"
            pre = i
            num+=1
            if (num == m) :
                break
        else :
            str+="0"
    
    while(len(str) < k) : 
        str+="0"
        
   
    if(num == m) :
        start = mid+1
        fin = str
    else :
        end = mid-1

        
print(fin)
# 중앙값이 크면 심판배치 적고, 작을 경우 심판 많음
# 중앙값보다 큰값을 거리로 가질 때 심판이 다 구해지면 종료
