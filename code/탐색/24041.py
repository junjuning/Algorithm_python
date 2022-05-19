## 골드 4
# 파라메트릭 서치
# 이분탐색

import sys

n, g, k = map(int, input().split())

meal = [] # 안들어가도 되는 경우
fin = [] # 무조건 들어가야 하는 경우

for _ in range(n):
    food= list(map(int, sys.stdin.readline().split()))
    if(food[2]==0):
        fin.append(food)
    else:
        meal.append(food)

start = 0
end = 2 * 10 ** 9 + 1
result = 0
while(start<=end): 
    mid = (start+end)//2
    totalsum = 0 

    for i in fin:
        totalsum+=i[0]*max(1, mid-i[1])
    vac=[]
    for i in meal:
        vac.append(i[0]*max(1, mid-i[1]))
    vac.sort()

    if((totalsum+sum(vac[:len(vac)-k]) <= g)): 
        result = mid
        start = mid+1
        
    else:
        end = mid-1

print(result)


# 무엇을 이진탐색으로 잡아야 할까
# 날을 이진탐색