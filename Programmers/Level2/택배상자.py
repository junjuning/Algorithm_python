from collections import deque
def solution(order):
    num = len(order)
    arr = deque()
    for i in range(1, num + 1):
        arr.append(i)
    temp = []
    target = 0
    
    while True:
        if arr and order[target] == arr[0]:
            arr.popleft()
            target += 1
            continue
            
        elif temp and order[target] == temp[-1]:
            temp.pop()
            target += 1
            continue
        elif arr:
            now = arr.popleft()
            temp.append(now)
            continue
        break
    return target
