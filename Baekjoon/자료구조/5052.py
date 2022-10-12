import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(sys.stdin.readline().strip())

    arr.sort()


    for i in range(len(arr) - 1):
        if(arr[i] in arr[i+1][:len(arr[i])]):
            print('NO')
            break
        if(i == len(arr)-2):
            print('YES')
