# 그리디
# 리스트에서 pop은 매개변수를 넣을 수 없음. 해당값을 지우고 싶다면 remove 사용
# 배열-배열을 하고 싶다면 set사용

def solution(n, lost, reserve):
    answer = 0
    newLost = set(lost)-set(reserve)
    newReserve = set(reserve)-set(lost)
    
    for i in newReserve:
        front = i - 1
        behind = i + 1
        
        if(front in newLost):
            newLost.remove(front)
        elif(behind in newLost):
            newLost.remove(behind)
        
    answer = (n - len(newLost))
    return answer