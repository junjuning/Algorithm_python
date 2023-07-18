from collections import deque
def solution(maps):
    answer = []
    row = len(maps[0])
    col = len(maps)
    
    
    visited = [[0 for _ in range(row)] for _ in range(col)]
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    print(visited)
    q = deque()
    
    def bfs(y, x):
        q.append([x, y])
        sum = int(maps[y][x])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < row and 0 <= ny < col and visited[ny][nx] == 0 and maps[ny][nx] != 'X':
                    q.append([nx, ny])
                    visited[ny][nx] = 1
                    sum += int(maps[ny][nx])
        return sum
                    
        
    for i in range(col):
        for j in range(row):
            if visited[i][j] == 0 and maps[i][j] != 'X':
                visited[i][j] = 1
                sum = bfs(i, j)
                answer.append(sum)
    
    if answer:
        return sorted(answer)
    else:
        return [-1]