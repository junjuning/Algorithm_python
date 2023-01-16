# counter 라이브러리 사용

import collections

def solution(clothes):
    answer = 1
    type =[]
    for i in clothes:
        type.append(i[1])
    count = list(collections.Counter(type).values())  
    for j in range(len(count)):
            answer = (answer*((count)[j]+1)) 
        
    return (answer-1)  
