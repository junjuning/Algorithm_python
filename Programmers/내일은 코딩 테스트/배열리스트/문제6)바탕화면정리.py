def solution(wallpaper):
    answer = []
    y = len(wallpaper)
    x = len(wallpaper[0])
    sx = x
    sy = y
    ex = -1
    ey = -1
    for i in range(y):
        if "#" in wallpaper[i]:
            sx = min(wallpaper[i].index("#"), sx)
            sy = min(i, sy)

    for i in range(y - 1, -1, -1):
        if "#" in wallpaper[i]:
            ex = max(wallpaper[i].rfind("#"), ex)
            ey = max(i, ey)
    return [sy, sx, ey + 1, ex + 1]