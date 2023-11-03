import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))


a.sort()
b.sort(reverse = True)
answer = 0
for i in range(n):
    answer += a[i] * b[i]
print(answer)
