
from collections import deque
def solution(ingredient):
    answer = 0
    stack = []
    arr = [1, 2, 3, 1]
    num = 0
    
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == arr:
            for i in range(4):
                stack.pop()
            answer += 1
            
    return answer