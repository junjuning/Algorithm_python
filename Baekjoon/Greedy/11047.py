import sys
n, k = map(int, sys.stdin.readline().split(' '))
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
    
arr.sort(reverse = True)
answer = 0
for i in arr:
    if i <= k:
        answer += k // i
        k = k % i

print(answer)