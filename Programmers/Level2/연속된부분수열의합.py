def solution(sequence, k):
    answer = []
    min = len(sequence)
    
    arr = [sequence[0]]
    if arr[0] == k:
        return [0, 0]
    left = 0
    for right in range(1, len(sequence)):
        if sequence[right] == k:
            return [right, right]
        if sequence[right] > k:
            break
        arr.append(arr[right - 1] + sequence[right])
        now = arr[right]
        while now >= k and left <= right:
            if now == k:
                if min > right - left:
                    answer = [left, right]
                    min = right - left
            now -= sequence[left]
            arr[right] -= sequence[left]
            left += 1
    return answer
    
    
#     arr = [[0 for _ in range(len(sequence))] for _ in range(len(sequence))]
    
#     for i in range(len(sequence)):
#         for j in range(i, len(sequence)):
#             if i == j:
#                 sum = sequence[i]
#             else:
#                 sum = arr[i][j - 1] + sequence[j]
#             arr[i][j] = sum
#             if sum == k:
#                 answer.append([i, j])
    
#     min = len(sequence)
#     sorted(answer)
#     for i, j in answer:
#         if min > j - i:
#             min = j - i
#             result = [i, j]
#     return result
