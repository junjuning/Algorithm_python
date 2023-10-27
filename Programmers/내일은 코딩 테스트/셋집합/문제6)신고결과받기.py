from collections import Counter
def solution(id_list, report, k):
    answer = {}
    dic = {}
    result = []
    for i in id_list:
        dic[i] = []
        answer[i] = 0
        
    for i in report:
        a, b = i.split(' ')
        if a not in dic[b]:
            result.append(b)
            dic[b].append(a)
        
    result = dict(Counter(result))
    result = [i for i, j in result.items() if j >= k]
    for i in result:
        for j in dic[i]:
            answer[j] += 1

    return list(answer.values())