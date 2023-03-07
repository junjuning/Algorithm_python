from collections import deque
from collections import Counter
def solution(s):
    arr = []
    q = deque(s)
    num = []
    for i in range(1, len(s) - 1):
        now = q.popleft()
        if now == '{':
            continue
        elif now == '}':
            continue
        elif now == ',':
            arr.append(''.join(num))
            num = []
        else:
            num.append(now)

    arr.append(''.join(num))
    counter = Counter(arr)
    counter = sorted(counter.items(), key = lambda x: x[1], reverse = True)
    counter = list(map(int, list(dict(counter).keys())))

    return counter