from collections import Counter
def solution(S):
    # Implement your solution here
    counter = Counter(S)
    answer = 0
    print(counter)
    for cnt in counter.values():
        print(cnt)
        if cnt % 2 != 0:
            answer += 1
    pass

solution("acbcbbaacb")