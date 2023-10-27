from collections import deque
def solution(spell, dic):
    for target in dic:
        q = deque(spell)
        for i in target:
            if i not in q:
                break
            q.remove(i)
        if not q and len(target) == len(spell):
            return 1
    return 2