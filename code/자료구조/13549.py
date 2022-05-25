from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n) 
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    x = q.popleft()
    if x == k:
        print(visited[x])
        break
    if 0 <= x-1 < 100001 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
    if 0 < x*2 < 100001 and visited[x*2] == -1:
        visited[x*2] = visited[x]
        q.appendleft(x*2)  # 2*x 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= x+1 < 100001 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)
