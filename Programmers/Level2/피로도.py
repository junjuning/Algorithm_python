## 완전탐색을 dfs로 풀어야겠다는 접근은 좋았음
# 완전탐색해야하니 재귀보내고 방문기록이나 줄어든 k값을 원상복귀 시켜줘야하는게 포인트

answer = 0            

def dfs(k, cnt, visit, dungeons):
    global answer
    answer = max(answer, cnt)
        
    for i in range(len(dungeons)):
        if visit[i] == 0 and dungeons[i][0] <= k:
            visit[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, visit, dungeons)
            visit[i] = 0
            
def solution(k, dungeons): 
    visit = [0 for _ in range(len(dungeons))]
    dfs(k, 0, visit, dungeons)
    return answer