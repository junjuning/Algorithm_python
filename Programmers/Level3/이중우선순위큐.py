def solution(operations):
    answer = []
    arr = []
    for i in operations:
        arr.sort(reverse = True)
        if i[0] == 'I':
            arr.append(int(i[2:]))
        elif arr:
            if i == "D 1":
                arr.pop(0)
            elif i == "D -1":
                arr.pop(-1)
    if not arr:
        return [0, 0]
    else:
        return [max(arr), min(arr)]
