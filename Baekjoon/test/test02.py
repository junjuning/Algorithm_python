import math

def minimum_cost(n, pencil):
    # DP를 위한 배열 초기화
    # dp[i]는 i개 이상의 연필을 구매하는 데 필요한 최소 비용
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # 묶음당 금액이 작은 순서대로 정렬
    pencil.sort(key=lambda x: x[1] // x[0])

    # DP 진행
    for i in range(1, n + 1):
        print(i)
        for j in range(len(pencil)):
            # i개 이상의 연필을 구매할 수 있는 경우
            dp[i] = min(dp[i], (i // pencil[j][0] + 1) * pencil[j][1])
            if i >= pencil[j][0]:
                dp[i] = min(dp[i], dp[i - pencil[j][0]] + pencil[j][1])
                # 정렬된 순서대로 구매하므로, 해당 연필 회사에서 더 이상 구매하지 않고 종료
        print(dp)

    return dp[n]

print(minimum_cost(3, [[6, 30000], [3, 18000], [4, 28000], [1, 9500]]))