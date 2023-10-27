from collections import deque
def solution(priorities, location):
    answer = 1
    arr = deque([i,priorities[i]] for i in range(len(priorities)))

    target = max(priorities)
    while arr:
        i, j = arr.popleft()
        if j == target:
            if i == location:
                return answer
            priorities.remove(target)
            target = max(priorities)
            answer += 1
        else:
            arr.append([i, j])

    return answer