def solution(record):
    answer = []
    people = {}
    for i in record:
        arr = i.split()
        if arr[0] != 'Leave':
            people[arr[1]] = arr[2]
    
    for i in record:
        arr = i.split()
        if arr[0] == 'Enter':
            answer.append(people[arr[1]] + "님이 들어왔습니다.")
        elif arr[0] == 'Leave':
            answer.append(people[arr[1]] + "님이 나갔습니다.")
            
    return answer