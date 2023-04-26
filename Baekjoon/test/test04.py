def solution(kor, usa, incs):
    kor_dict = {}
    usa_dict = {}
    for stock in kor:
        kor_dict[stock] = set()
    for stock in usa:
        usa_dict[stock] = set()
    for day, inc_list in enumerate(incs):
        print(day, inc_list)
        inc_set = set(inc_list.split())
        for stock in kor_dict.keys():
            if stock in inc_set:
                kor_dict[stock].add(day)
        for stock in usa_dict.keys():
            if stock in inc_set:
                usa_dict[stock].add(day)
    max_days = 0
    for kor_stock, kor_days in kor_dict.items():
        for usa_stock, usa_days in usa_dict.items():
            common_days = len(kor_days & usa_days)
            if common_days > max_days:
                max_days = common_days
    return max_days

print(solution(["AAA", "BCD", "AAAAA", "ZY"], ["AB", "AA", "TTTT"], ["AB BCD AA AAA TTTT AAAAA", "BCD AAA", "AB AAA TTTT BCD", "AA AAAAA AB", "AAA AB BCD"]))