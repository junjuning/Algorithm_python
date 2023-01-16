# bfs

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0:
            bfs(n, computers, i, visited)
            answer += 1
    return answer

def bfs(n, computers, now, visited):
    visited[now] = 1
    q = []
    q.append(now)
    while (q):
        now = q.pop(0)
        visited[now] = 1
        for i in range(n):
            if i != now and computers[now][i] == 1:
                if visited[i] == 0:
                    q.append(i)