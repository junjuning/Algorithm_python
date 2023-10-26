def solution(id_pw, db):
    dict = {item[0]:item[1] for item in db}
    
    if id_pw[0] not in dict.keys():
        return "fail"
    elif dict[id_pw[0]] == id_pw[1]:
        return "login"
    else:
        return "wrong pw"
    