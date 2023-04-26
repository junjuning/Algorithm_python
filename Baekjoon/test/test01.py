def solution(num, arr):
    slow = arr[0]
    # 두 번째 포인터는 두 칸씩 이동합니다.
    fast = arr[arr[0]]
    # 사이클을 찾을 때까지 반복합니다.
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    # 첫 번째 포인터를 배열의 시작 위치로 이동합니다.
    slow = 0
    # 첫 번째 포인터와 두 번째 포인터를 한 칸씩 이동하면서, 만날 때까지 각각 이동합니다.
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    # 사이클의 시작 위치를 기록합니다.
    cycle_start = slow
    # 사이클의 원소들을 기록합니다.
    cycle_elements = [cycle_start]
    slow = arr[cycle_start]
    while slow != cycle_start:
        cycle_elements.append(slow)
        slow = arr[slow]
    # 기록된 원소들을 반환합니다.
    print(cycle_elements)
    return cycle_elements

solution(3, [1, 2, 3, 1])