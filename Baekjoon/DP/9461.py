## 실버 3

arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49]

i = int(input())

for _ in range(i):
    n = int(input())
    if n >= len(arr):
        for i in range(len(arr), n + 1):
            arr.append(arr[i - 1] + arr[i - 5])
            
    print(arr[n])
