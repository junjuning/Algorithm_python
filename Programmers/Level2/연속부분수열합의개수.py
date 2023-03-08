def solution(elements):
    answer = 0
    arr= set()
    num = len(elements)
    for i in range(1, num + 1):
        for j in range(num):
            arr.add(sum(elements[0:i]))
            now = elements.pop(0)
            elements.append(now)
    return len(set(arr))