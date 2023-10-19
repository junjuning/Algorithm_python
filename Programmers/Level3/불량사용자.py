from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    
    userList = list(permutations(user_id, len(banned_id)))
    
    
    def check(users):
        for i in range(len(banned_id)):
            if len(users[i]) != len(banned_id[i]):
                return 0
            for j in range(len(users[i])):
                if banned_id[i][j] == '*':
                    continue
                if users[i][j] != banned_id[i][j]:
                    return 0
                
    for users in userList:
        result = check(users)
        if result == 0:
            continue

        if set(users) not in answer:
            answer.append(set(users))
    
    return len(answer)