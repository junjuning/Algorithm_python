from itertools import product

def solution(word):
    answer = []
    char = ["A", "E", "I", "O", "U"]
    for i in range(1, 6):
        for j in product(char, repeat = i):
            answer.append(''.join(list(j)))
    answer.sort()
    return answer.index(word) + 1