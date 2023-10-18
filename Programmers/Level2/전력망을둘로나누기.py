from collections import Counter
def solution(n, wires):
    answer = n
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    for i, j in wires:
        arr[i - 1][j - 1] = 1
        arr[j - 1][i - 1] = 1
    
    def bfs(x, y):
        no = [x, y]
        while q:
            now = q.pop()
            for i in range(1, n + 1):
                if i != now and visit[i - 1] != 1:
                    if arr[now - 1][i - 1] == 1 and (now not in no or i not in no):
                        q.append(i)
                        visit[i - 1] = 1
    
    for i, j in wires:
        visit = [0] * n
        q = [1]
        visit[0] = 1
        bfs(i, j)
        count = Counter(visit)
        answer = min(answer, abs(count[0] - count[1]))
    
    return answer