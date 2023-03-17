# 야심차게 bfs로 풀었다가 개같이 멸망
# 캐싱이 안된다는 점이 dp를 사용해야 하는 이유인듯

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j +1:])
    return max(land[len(land)-1])
    
#     for i in range(4):
#         q.append([0, i, 0])
    
#     while q:
#         x, y, score = q.popleft()
#         if x + 1 == len(land):
#             if answer < score + land[x][y]:
#                 answer = score + land[x][y]
#         else:
#             for i in range(4):
#                 if i == y:
#                     continue
#                 else: 
#                     q.append([x + 1, i, score + land[x][y]])
    
#     return answer