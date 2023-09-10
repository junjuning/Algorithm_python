def solution(book_time):
    book_time.sort(key = lambda x: x[0])
    arr = [0]
    for start, end in book_time:
        arr.sort()
        h, m = start.split(":")
        start_time = int(h) * 60 + int(m)
        h, m = end.split(":")
        end_time = int(h) * 60 + int(m)
        for i in range(len(arr)):
            if arr[i] <= start_time:
                arr[i] = end_time + 10
                break
            if i == len(arr) - 1:
                arr.append(end_time + 10)
    return len(arr)