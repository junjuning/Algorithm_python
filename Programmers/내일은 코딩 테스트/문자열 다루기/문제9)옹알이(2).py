def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    
    for string in babbling:
        target = ""
        before = "-1"
        for i in string:
            target += i 
            if target in arr and target != before:
                before = target
                target = ""
        if not target:
            answer += 1
    return answer