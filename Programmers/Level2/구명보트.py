# 그리디
# 투포인터

def solution(people, limit):
    answer = 0
    people.sort()
    a = 0
    b = len(people) - 1
    
    while a <= b:
        if people[b] + people[a] <= limit:
            a += 1
        b -= 1
        answer += 1
        if a == b:
            answer +=1
            a += 1
    return answer