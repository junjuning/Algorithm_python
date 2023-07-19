def solution(m, musicinfos):
    answer = {}
    arr = {'Z':'C#', 'X':'D#', 'Q':'F#', 'W':'G#', 'R':'A#'}
    
    print(m)
    for key, value in arr.items():
        m = m.replace(value, key)
    
    for musicinfo in musicinfos:
        start, end, name, melody = musicinfo.split(',')
        
        for key, value in arr.items():
            melody = melody.replace(value, key)
        
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        if sm > em:
            time = (em + 60 - sm) + (eh - sh - 1)* 60
        else:
            time = (em - sm) + (eh - sh)* 60

        line = ((time // len(melody) + 1) * melody)[:time]
        
        if m in line:
            answer[name] = time
        
    if not answer:
        return "(None)"
    answer = sorted(answer.items(), key = lambda x: x[1], reverse = True)
    return answer[0][0]