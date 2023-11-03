import sys
n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
    
arr.sort()

answer = 0
for i in range(n):
    answer = max(answer, arr[i] * (n - i))

print(answer)