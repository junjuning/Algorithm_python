## 실버3
# 예외처리 생각도 못했다

n = int(input())
stair = [0]
arr = [0 for _ in range(n+2)]
for i in range(n):
    stair.append(int(input()))

if n>=3:
    arr[0] = stair[0]
    arr[1] = stair[1]
    arr[2] = stair[1] + stair[2]
    arr[3] = max(stair[1] + stair[3], stair[2] + stair[3])

    for i in range(4, n+1):
        arr[i] = max(arr[i-3] + stair[i-1] + stair[i], arr[i-2] + stair[i])

    print(arr[n])

elif n==2:
    print(stair[1] + stair[2])

elif n==1:
    print(stair[1])
