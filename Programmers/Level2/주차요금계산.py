import math
def solution(fees, records):
    answer = {}
    result = []
    arr = []
    for record in records:
        time, num, status = record.split(' ')
        arr.append([time, num, status])
    arr.sort(key = lambda x: x[1])
    
    def cal():
        if flag[1] == -1:
            end = 23 * 60 + 59
            answer[flag[0]] += end - start
        cost = 0
        if flag[0] in answer:
            if answer[flag[0]] <= fees[0]:
                cost += fees[1]
                result.append(cost)
            else:
                cost += fees[1]
                answer[flag[0]] = answer[flag[0]] - fees[0]
                cost += math.ceil(answer[flag[0]] / fees[2]) * fees[3]
                result.append(cost)
                    
    flag = [arr[0][1], -1]
    for time, num, status in arr:
        h, m = time.split(':')
        t = int(h) * 60 + int(m)
        
        if flag[0] != num:
            cal()
                
        if status == "IN":
            start = t
            if num not in answer:
                answer[num] = 0
            flag = [num, -1]
        else:
            park = t - start
            answer[num] += park
            flag = [num, 0]
    cal()
    return result