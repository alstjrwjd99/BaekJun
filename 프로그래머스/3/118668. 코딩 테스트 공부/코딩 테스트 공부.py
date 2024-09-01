def solution(alp, cop, problems):
    max_alp = max([p[0] for p in problems])
    max_cop = max([p[1] for p in problems])
    
    # 현재 alp와 cop가 목표보다 높을 경우를 대비
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    # DP 테이블 초기화
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 1씩 증가시키는 경우
            if i < max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            
            # 문제를 푸는 경우
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(max_alp, i + alp_rwd)
                    new_cop = min(max_cop, j + cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
    
    return dp[max_alp][max_cop]