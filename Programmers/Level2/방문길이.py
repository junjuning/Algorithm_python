def solution(dirs):
    visit = []
    nowx = 5
    nowy = 5
    
    for i in dirs:
        if i == "U":
            y = nowy + 1
            if y > 10:
                continue
            if [nowx, nowy, nowx, y] not in visit and [nowx, y, nowx, nowy] not in visit:
                visit.append([nowx, nowy, nowx, y])
            nowy = y
        elif i == "D":
            y = nowy - 1
            if 0 > y:
                continue
            if [nowx, nowy, nowx, y] not in visit and [nowx, y, nowx, nowy] not in visit:
                visit.append([nowx, nowy, nowx, y])
            nowy = y     
        elif i == "R":
            x = nowx + 1
            if x > 10:
                continue
            if [nowx, nowy, x, nowy] not in visit and [x, nowy, nowx, nowy] not in visit:
                visit.append([nowx, nowy, x, nowy])
            nowx = x   
        elif i == "L":
            x = nowx - 1
            if x < 0:
                continue
            if [nowx, nowy, x, nowy] not in visit and [x, nowy, nowx, nowy] not in visit:
                visit.append([nowx, nowy, x, nowy])
            nowx = x
                             
    return len(visit)