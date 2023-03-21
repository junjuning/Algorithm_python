# 최단 거리를 계속 더하면서 나아가야함

from collections import deque

def solution(maps):
    q = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0] # 하 상 우 좌 
    
    answer = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    n = len(maps[0])
    m = len(maps)
    q.append([0, 0])
    answer[0][0] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and maps[ny][nx] == 1:
                if answer[ny][nx] == -1:
                    answer[ny][nx] = answer[y][x] + 1
                    q.append([nx, ny])

    return answer[-1][-1]