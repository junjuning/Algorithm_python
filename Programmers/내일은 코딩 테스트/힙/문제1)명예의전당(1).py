def solution(k, score):
    answer = []
    board = []
    
    for i in score:
        board.append(i)
        board.sort(reverse = True)
        board = board[:k]
        answer.append(board[-1])
    return answer