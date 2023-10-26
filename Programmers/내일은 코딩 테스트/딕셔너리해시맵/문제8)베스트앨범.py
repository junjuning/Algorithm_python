def solution(genres, plays):
    answer = []
    dic = {}
    arr = []
    for i in range(len(genres)):
        arr.append([i, genres[i], plays[i]])
        
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = plays[i]
    dic = dict(sorted(dic.items(), key = lambda x: x[1], reverse = True))
    
    for k in dic.keys():
        temp = []
        for i, g, p in arr:
            if g == k:
                temp.append([i, g, p])
        temp = sorted(temp, key = lambda x:(-x[2], x[0]))
        now = []
        for i in range(len(temp)):
            if len(now) == 2:
                break
            now.append(temp[i][0])
        answer += now
    return answer