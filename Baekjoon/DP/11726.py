## 실버 3

n = int(input())

arr = [1, 2]
for i in range(2, n):
    arr.append(arr[i-1] + arr[i-2])
    
print(arr[n-1]%10007)