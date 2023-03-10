# BFS, 쉬운편
# 모든 숫자를 사용하는지 확인하기 위해 큐에 사용한 숫자의 개수를 넣어야 했음
# 방문한 곳을 체크하지 않아도 되는 문제

from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque()
    q.append([0, -1])
    length = len(numbers) - 1
    
    while q:
        sum, idx = q.popleft()
        if idx <= length:
            if idx == length and sum == target:
                answer += 1
            q.append([sum + numbers[idx], idx + 1])
            q.append([sum - numbers[idx], idx + 1])
    return answer