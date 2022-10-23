## 실버 5

n = int(input())
arr = []

arr.append(0)
arr.append(1)

for i in range(2, n+1):
    arr.append(arr[i-1] + arr[i-2])
    
print(arr[n])