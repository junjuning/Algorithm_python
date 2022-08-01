from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([0, 0])
    
    while q:
        x, l = q.popleft()
        if(l>len(numbers)):
            break
        if(x == target and l == len(numbers)):
            answer += 1
        q.append([x+numbers[l-1], l+1])
        q.append([x-numbers[l-1], l+1])
        
    return answer