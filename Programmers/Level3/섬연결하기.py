## 그리디
# 크러스컬 알고리즘

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    MST = set([costs[0][0]])

    while len(MST) < n:
        for i, j, cost in costs:
            if i in MST and j in MST:
                continue
            if i in MST or j in MST:
                MST.add(i)
                MST.add(j)
                answer += cost
                break
    return answer