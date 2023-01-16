## 실버 3
# 점화식만 세우면 쉽네

n = int(input())

arr = [0, 1, 3]
for i in range(3, n+1):
    arr.append(arr[i-1]+2*arr[i-2])

print(arr[n]%10007)
