# BFS 문제 중 쉬운편
# 모든 숫자를 사용하는지 확인하기 위해 큐에 사용한 숫자의 개수를 넣어야 했음
# 방문한 곳을 체크하지 않아도 되는 문제

from collections import deque

def solution(numbers, target):
    answer = 0
    length = len(numbers)
    q = deque()
    q.append([0, 0])
    
    while q:
        x, l = q.popleft()
        if(l<=length):
            if(x == target and l == length):
                answer += 1
            q.append([x+numbers[l-1], l+1])
            q.append([x-numbers[l-1], l+1])
    return answer