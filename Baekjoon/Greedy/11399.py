import sys
n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse = True)

answer = 0
for i in range(n):
    answer += arr[i] * (i + 1)
    
print(answer)
