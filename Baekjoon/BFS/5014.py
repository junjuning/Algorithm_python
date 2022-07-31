## 골드 5
# 사실 잘 모르고 푼 느낌. bfs 공부가 더 필요

from collections import deque
f, s, g, u, d = map(int, input().split())
visited = [0 for i in range(f+1)]

def bfs():
    q = deque()
    q.append(s)
    visited[s]=1
    while(q):
        now=q.popleft()
        if(now==g):
            print(visited[g]-1)
            return 0
        if(now+u<=f and visited[now+u]==0):
            visited[now+u]=visited[now]+1
            q.append(now+u)
        if(now-d>0 and visited[now-d]==0):
            visited[now-d]=visited[now]+1
            q.append(now-d)

    else:
        print('use the stairs')
        return 0

bfs()
