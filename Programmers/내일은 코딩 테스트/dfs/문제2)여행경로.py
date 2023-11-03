from collections import deque
def solution(tickets):
    global result
    result = []
    
    tickets.sort(key = lambda x: (x[0], x[1]))
    
    def dfs(tickets, start, answer):
        if not tickets:
            answer.append(start)
            result.append(answer)
        for i in range(len(tickets)):
            if tickets[i][0] == start:
                now = deque(tickets)
                del now[i]
                dfs(now, tickets[i][1], answer + [start])
        
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            now = deque(tickets)
            del now[i]
            dfs(now, tickets[i][1], ["ICN"])
        if result:
            return result[0]