def solution(survey, choices):
    answer = ''
    dict = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for i in range(len(survey)):
        l = survey[i][0]
        r = survey[i][1]
        score = choices[i]
        
        if score < 4:
            dict[l] += 4 - score
        elif score > 4:
            dict[r] += score - 4
    

    if dict["R"] < dict["T"]:
        answer += "T"
    else:
        answer += "R"
    if dict["C"] < dict["F"]:
        answer += "F"
    else:
        answer += "C"
    if dict["J"] < dict["M"]:
        answer += "M"
    else:
        answer += "J"
    if dict["A"] < dict["N"]:
        answer += "N"
    else:
        answer += "A"

    return answer