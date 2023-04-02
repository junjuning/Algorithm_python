## 실버 5

n = int(input())

for _ in range(n):
    son = 1
    par = 1
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        par *= m + 1 - i
        son *= i
        
    print(par//son)