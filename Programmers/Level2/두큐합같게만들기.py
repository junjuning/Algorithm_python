from collections import deque
def solution(queue1, queue2):
    answer = -2
    cnt=0
    queue1, queue2 = deque(queue1), deque(queue2)
    target = sum(queue1) + sum(queue2) // 2
    while queue1 and queue2:
        if(sum(queue1) == sum(queue2)):
            return cnt
        elif(sum(queue1)>target):
            queue2.append(queue1.popleft())
        else:
            queue1.append(queue2.popleft())
        cnt+=1
        
    return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))