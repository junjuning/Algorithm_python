from collections import deque
from collections import Counter

def solution(n, edge):
    answer = 0
    arr = [[] for _ in range(n + 1)]
    visit = [-1] * (n + 1)
    
    for i, j in edge:
        arr[i].append(j)
        arr[j].append(i)
    
    q = deque()
    q.append(1)
    visit[1] = 0
    while q:
        x = q.popleft()
        for i in arr[x]:
            if visit[i] == -1:
                visit[i] = visit[x] + 1
                q.append(i)
    len = max(visit)
    visit = Counter(visit)
    return visit[len]