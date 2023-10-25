# def solution(babbling):
#     answer = 0
#     arr = ["aya", "ye", "woo", "ma"]
    
#     for string in babbling:
#         start = 0
#         flag = 0
#         while start < len(string):
#             flag = 0
#             for i in arr:
#                 now = string[start:start + len(i)]
#                 if i == now:
#                     start = start + len(i)
#                     flag = 1
#                     break
#             if flag == 0:
#                 break
#         if flag == 1:
#             answer += 1
    
#     return answer

def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    
    for string in babbling:
        target = ""
        for i in string:
            target += i
            if target in arr:
                target = ""
        if not target:
            answer += 1
    
    return answer