# 코드가 더럽지만,,다른사람 풀이를 보고 전의를 상실했다.

from collections import deque
def solution(s):
    answer = 0

    for i in range(len(s)):
        q = deque(s)
        arr = deque()
        for j in range(i):
            now = q.popleft()
            q.append(now)

        if q[0] == ']' or q[0] == '}' or q[0] == ')':
            continue
            
        arr.append(q.popleft())     
        while q:
            now = q.popleft()

            if now == ']' or now == '}' or now == ')':
                if arr:
                    if arr[-1] == '[':
                        if now != ']':
                            continue
                    elif arr[-1] == '{':
                        if now != '}':
                            continue
                    elif arr[-1] == '(':
                        if now != ')':
                            continue
                else:
                    continue
                arr.pop()
            else:
                arr.append(now)

        if arr:
            continue
        else:
            answer += 1
            
            
    return answer