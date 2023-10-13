from itertools import permutations
import math
def solution(numbers):
    answer = 0
    arr = []
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(numbers, i))
        for j in temp:
            n = ''.join(j) 
            arr.append(int(n))
    arr = set(arr)
    for i in arr:
        flag = 1
        if i == 0 or i == 1:
            flag = 0
            continue
        
        for j in range(2, round(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            answer += 1
        
    return answer