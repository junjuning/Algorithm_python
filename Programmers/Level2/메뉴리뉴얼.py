from itertools import combinations
def solution(orders, course):
    answer = []
    
    for j in course:
        dict = {}
        for i in range(len(orders)):
            combi = list(combinations(sorted(orders[i]), j))
            for k in combi:
                if k in dict:
                    dict[k] += 1
                else:
                    dict[k] = 1

        for k,v in dict.items():
            if max(dict.values()) == v and v >= 2:
                answer.append(''.join(k))

    return sorted(answer)