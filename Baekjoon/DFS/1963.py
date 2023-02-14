## 골드4
# 소수 구하는게 포인트

from collections import deque
import sys
sys.setrecursionlimit(99999)

t = int(input())
prime = [True for _ in range(10000)]

def findPrime():
    for i in range(2, 100):
        if prime[i]:
            for j in range(2*i,  10000, i):
                prime[j] = False
                
findPrime()

def bfs():
    while q:
        num, cnt = q.popleft()
        if num == after:
            return cnt
        for i in range(4):
            for j in range(10):
                temp = int(str(num)[:i] + str(j) + str(num)[i+1:])
                if visit[temp] == 0 and prime[temp] and temp > 999:
                    visit[temp] = 1
                    q.append([temp, cnt + 1])


for _ in range(t):
    visit = [0 for _ in range(10000)]
    before, after = map(int, sys.stdin.readline().split())
    q = deque()
    q.append([before, 0])
    
    result = bfs()
    if result == None:
        print("Impossible")
    else:
        print(result)