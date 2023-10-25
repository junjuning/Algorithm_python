import re
from itertools import permutations
from collections import deque
def solution(expression):
    answer = []
    op = list(permutations(['+','-','*'],3))
    expression = re.split("([^0-9])", expression)

    for os in op:
        s = deque(expression)
        exp = deque(expression)
        for o in os:
            for i in range(len(exp)):
                now = s.popleft()
                if s and o == s[-1]:
                    s.pop()
                    if o == '*':
                        s.append(int(now) * int(s.pop()))
                    elif o == '+':
                        s.append(int(now) + int(s.pop()))
                    elif o == '-':
                        s.append(int(s.pop()) - int(now))
                else:
                    s.append(now)
            exp = s
        answer.append(abs(s[0]))
    return max(answer)