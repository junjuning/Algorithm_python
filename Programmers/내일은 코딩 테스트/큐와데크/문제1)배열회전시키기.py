## deque.rotate(n) -> n만큼 회전시키기

from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)


# def solution(numbers, direction):
#     numbers = deque(numbers)
    
#     if direction == "right":
#         now = numbers.pop()
#         numbers.insert(0, now)
#     else:
#         now = numbers.popleft()
#         numbers.append(now)
#     return list(numbers)