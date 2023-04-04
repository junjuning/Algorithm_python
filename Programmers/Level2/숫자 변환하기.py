from collections import deque

def solution(x, y, n):
    arr = [y-x for _ in range(y + 1)]
    
    arr[x] = 0

    if x == y:
        return 0
    
    for i in range(x, y + 1):
        if i + n <= y:
            arr[i + n] = min(arr[i] + 1, arr[i + n])
        if i * 2 <= y:
            arr[i * 2] = min(arr[i] + 1, arr[i * 2])
        if i * 3 <= y:
            arr[i * 3] = min(arr[i] + 1, arr[i * 3])

    if arr[y] == y-x:
        return -1
    return arr[y]


#     q = deque()
#     q.append([x, 0])
#     while q:
#         now, cnt = q.popleft()
#         if now >= y:
#             if now == y and answer > cnt:
#                 answer = cnt
#             continue
#         q.append([now + n, cnt + 1])
#         q.append([now * 2, cnt + 1])
#         q.append([now * 3, cnt + 1])
    
#     if answer == y - x:
#         return -1
    # return answer