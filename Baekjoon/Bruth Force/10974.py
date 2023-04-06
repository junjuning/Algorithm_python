## 실버 3
# 배열 앞에 * 붙이면 원소만 꺼내주는구나,,

n = int(input())

temp = []

def dfs():
    print(temp)
    if len(temp) == n:
        print(*temp)
        return
    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()
            
dfs()