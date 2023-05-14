def solution(genres, plays):
    answer = []
    arr = []
    for i in range(len(genres)):
        arr.append([genres[i], plays[i], i])
    
    dict = {}
    for i in range(len(genres)):
        if genres[i] not in dict.keys():
            dict[genres[i]] = plays[i]
        else:
            dict[genres[i]] += plays[i]
    dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)

    for genre in dict:
        s = []
        t = []
        for i, j, k in arr:
            if genre[0] == i:
                s.append([i, j, k])
        s.sort(key = lambda x:x[1], reverse = True)
        
        if len(s) == 1:
            t.append(s[0][2])
        else:  
            t.append(s[0][2])
            t.append(s[1][2])
            if s[0][1] == s[1][1]:
                t.sort()
        answer += t
        
    return answer