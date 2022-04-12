## 실버 2
# 우선순위 큐
# 리스트를 우선순위 큐로 변환해주는 heapify
# 리스트로 풀어도 성공은 함

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

## 첫번째 풀이
# card = sorted(card)
# sum=0
# for i in range(m):
#     a = card.pop(0)
#     b = card.pop(0)
#     card.append(a+b)
#     card.append(a+b)
#     card = sorted(card)
# for i in card:
#     sum += i
# print(sum)


## 두번째 풀이
# for i in range(m): 
#     card.sort()
#     card[0] = card[1] = card[0] + card[1]
    
# print(sum(card))

## 우선순위 큐
heapq.heapify(card) # 리스트를 heap으로 변환해준다고 함

for i in range(m):
    popCard=heapq.heappop(card)+heapq.heappop(card)
    heapq.heappush(card, popCard)
    heapq.heappush(card, popCard)
    
print(sum(card))