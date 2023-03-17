## 할인 상품이 더 많아도 될 줄 알았는데 number의 길이가 항상 10이므로 같을때만 되네,,이중루프 안써도 될뻔

from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        arr = Counter(discount[i:i+10])
        key = list(arr.keys())
        num = 0
        for j in range(len(want)):
            if want[j] in key:
                if number[j] == arr[want[j]]:
                    num += 1
            if num == len(want):
                answer += 1
    return answer