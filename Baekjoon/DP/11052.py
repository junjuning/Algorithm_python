import sys

n = int(input())


card = list(map(int, sys.stdin.readline().split()))


for i in range(n): 
    for j in range(i, n):
       


#점화식
#카드 1개 card[1]
#카드 2개 card[1]+max(card[1])