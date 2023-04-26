def count_groups_with_max_min_diff(a, max_min_diff):
    count = 1  # 첫번째 그룹은 항상 존재하므로 1로 초기화합니다.
    curr_min, curr_max = a[0], a[0]
    for num in a:
        curr_min = min(curr_min, num)
        curr_max = max(curr_max, num)
        if curr_max - curr_min > max_min_diff:
            curr_min, curr_max = num, num
            count += 1
    return count

def min_sum_of_differences(a, k):
    start, end = 0, max(a) - min(a)
    while start <= end:
        mid = (start + end) // 2
        if count_groups_with_max_min_diff(a, mid) <= k:
            end = mid - 1
        else:
            start = mid + 1
    return start




print(min_sum_of_differences([1, 2, 12, 14, 15], 2))