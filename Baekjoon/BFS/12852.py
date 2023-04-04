from collections import deque
n = int(input())
q = deque()
arr = [i for i in range(n + 1)]
arr[1] = 0
path  = [[] for i in range(n + 1)]
path[1] = [1]

for i in range(2, n + 1):
    arr[i] = arr[i - 1] + 1
    path[i] = path[i - 1] + [i]
    if i % 3 == 0 and arr[i] > arr[i//3] + 1:
        arr[i] =  arr[i//3] + 1
        path[i] = path[i//3] + [i]
    if i % 2  == 0 and arr[i] > arr[i//2] + 1:
        arr[i] = arr[i//2] + 1
        path[i] = path[i//2] + [i]

num = n
print(arr[n])
for i in path[i][::-1]:
    print(i, end = ' ')
# print(n, end = ' ')

# while num != 1:
#     print(path[num], end = ' ')
#     num = path[num]
    
    
    

## 시간초과,, 왤케 같은 실수를 반복할까
# def dfs(n, cnt, num):
#     if n == 1:
#         arr.append([cnt, num])
#         return 
#     if n % 3 == 0:
#         new_num = num[:]
#         new_num.append(n//3)
#         dfs(n//3, cnt + 1, new_num)
#     elif n % 2 == 0:
#         new_num = num[:]
#         new_num.append(n//2)
#         dfs(n//2, cnt + 1, new_num)
#     new_num = num[:]
#     new_num.append(n - 1)
#     dfs(n - 1, cnt + 1, new_num)
    
# dfs(n, 0, [n])

# arr.sort(key = lambda x: x[0])
# print(arr[0][0])
# print(' '.join(map(str, arr[0][1])))

