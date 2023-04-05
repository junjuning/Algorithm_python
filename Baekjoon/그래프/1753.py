## 골드 4
# 다익스트라
# 플로이셜 워셜은 메모리 초과

import heapq
import sys

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())

k = int(input())

arr = [[] for _ in range(V + 1)]
distance = [INF]*(V+1)
# visited = [False]*(V+1)

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append((v, w))

def dijkstra(start):
    q = [] # start부터 점까지의 거리들을 담음
    heapq.heappush(q, (0, start)) 
    distance[start] = 0 # 최단 경로
    
    while q:
        dist, now = heapq.heappop(q) # 최소힙이므로 최솟값 꺼내줌
        
        if distance[now] < dist: # 이미 방문했는지 확인. 처음을 무한으로 세팅했기 때문에 가능.
            continue
        for i in arr[now]: # now에서 인접한 노드들 
            next = dist + i[1] # start에서 now까지 온 거리 + now에서 인접한 노드까지의 거리 = start에서 인접한 노드까지의 거리

            if next < distance[i[0]]: #start에서 인접한 노드까지 한번에 오는것보다 짧으면 업데이트
                distance[i[0]] = next
                heapq.heappush(q, (next, i[0])) # start부터 i[0]까지의 거리가 next다.
    
dijkstra(k)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
        
## 플로이셜 워셜 알고리즘으로 품. 메모리 초과. 근데 다익스트라로 풀어도 되는 문제. 
# arr = [[11 for _ in range(V + 1)] for _ in range(V + 1)]


# for i in range(E):
#     u, v, w = map(int, sys.stdin.readline().split())
#     if arr[u][v] == 0:
#         arr[u][v] = w
#     else:
#         arr[u][v] = min(w, arr[u][v])

# for z in range(1, V + 1):
#     for i in range(1, V + 1):
#         for j in range(1, V + 1):
#             if i == j or i == z or z == j:
#                 continue
#             if arr[i][j] == 11 or (arr[i][z] == 11 and arr[z][i] == 11):
#                 arr[i][j] = min(arr[i][j], arr[i][z] + arr[z][j])
                

# for i in range(1, V + 1):
#     if i == k:
#         print(0)
#     elif arr[k][i] == 11:
#         print('INF')
#     else:
#         print(arr[k][i])