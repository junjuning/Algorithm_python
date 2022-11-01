import sys
n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
result = 0 

for i in range(n):
    if(arr[i] == m):
        result += 1
        continue
    sum = arr[i]
    for j in range(i+1, n):
        sum += arr[j]
        if(sum == m):
            result += 1
        elif(sum > m):
            break
        
print(result)