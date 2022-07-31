## 골드 4
# 브루트포스
# 꽤나 노가다.

import sys

n = int(input())

dice = [] 
for i in range(n):
    dice.append(list(map(int, sys.stdin.readline().split())))

max = max(dice[0]) #1~6
maxindex = dice[0].index(max) #0~5

peer = [5, 3, 4, 1, 2, 0] # 0~5
sumlist=[]
del max


for i in range(6): #0~5 i is index bottom is i
    sumdice = 0
    bott = i
    
    for j in range(n):
        allnum = [1, 2, 3, 4, 5, 6]
        top = peer[bott]
        if (dice[j][top] == 6 or dice[j][bott] ==6) :
            if (dice[j][top] == 5 or dice[j][bott] ==5):
                sumdice += 4
            else :
                sumdice += 5
        elif (dice[j][top] == 5 or dice[j][bott] ==5):
            if(dice[j][top] == 6 or dice[j][bott] ==6) :
                sumdice+=4
            else:
                sumdice+=6
        else:
            sumdice+=6        
        if(j<n-1):
            bott = dice[j+1].index(dice[j][top])
    sumlist.append(sumdice)
print(max(sumlist))

#a-f 0 5
#b-d 1 3
#c-e 2 4

# 최대값의 인덱스에 맞는 밑바닥 인덱스ㅡ, 윗면 을 찾ㅏㅑ 함
# 이때 밑면으로 올 수 있는값 자기 짝꿍빼고 4개
# 윗면과 같은 값ㅣ 밑바닥 올  때 윗면과 가장 큰  값 찾ㅏㅑ 함