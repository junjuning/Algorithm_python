## 실버2


n = input().split('-')
answer = []

for i in n:
    cnt = 0
    plus = list(map(int, i.split('+')))
    
    for j in plus:
        cnt += j
    answer.append(cnt)

result = answer[0]
for i in range(1, len(answer)):
    result -= answer[i]
    
print(result)
    