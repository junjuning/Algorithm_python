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

