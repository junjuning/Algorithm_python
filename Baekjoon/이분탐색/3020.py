import sys
n, h = map(int, input().split())
arr = [[0 for _ in range(h)] for _ in range(n)]
answer = [0 for _ in range(h-1)]
for i in range(n):
    now = int(sys.stdin.readline())
    add = [1] * now
    if i % 2 == 0:
        arr[i][:now] = add
    else:
        arr[i][h-now-1:] = add
 
print(arr)
print(answer)

# left = 0
# right = h - 1
# while True:
#     mid = (left + right) // 2
    