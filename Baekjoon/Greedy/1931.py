## 실버1
# 그리디 알고리즘
# 정렬 두번

n = int(input())
room = []

for i in range(n):
    room.append(list(map(int, input().split())))

room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

cnt=1

finish = room[0][1]

for i in range(1, n):
    if(finish<=room[i][0]):
        cnt+=1
        finish = room[i][1]

print(cnt)