def solution(s):
    answer = True
    cnt1 = 0
    cnt2 = 0

    for i in range(len(s)):
        if(s[i]==")"):
            cnt1 += 1
        elif(s[i]=="("):
            cnt2 += 1
        if(cnt1>cnt2):
            return False
            
    print(cnt1, cnt2)
    if(cnt1 == cnt2):
        return True
    else:
        return False


# def solution(s):
#     q = []
    
#     if s[0] == ')':
#         return False
#     q.append(s[0])
    
#     for i in range(1, len(s)):
#         if s[i] == '(':
#             q.append(s[i])
#         else:
#             if q:
#                 q.pop()
#             else:
#                 return False
#     if q:
#         return False
#     else:
#         return True
