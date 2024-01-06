def min_destroyed_power(n, agents):
    # agents[i][j]: i번째 요원이 j번째 능력치를 선택했을 때의 능력치 값
    # dp[mask][k]: mask 상태에서 k 능력치가 선택되었을 때의 최소 소멸 능력치
    INF = float('inf')
    dp = [[INF] * 3 for _ in range(1 << n)]

    # 초기값 설정
    for i in range(n):
        for j in range(3):
            dp[1 << i][j] = agents[i][j]

    # 동적 계획법을 통한 최소 소멸 능력치 계산
    for mask in range(1 << n):
        for last_power in range(3):
            if dp[mask][last_power] != INF:
                for i in range(n):
                    if (mask & (1 << i)) == 0:
                        next_mask = mask | (1 << i)
                        for next_power in range(3):
                            if last_power != next_power:
                                dp[next_mask][next_power] = min(dp[next_mask][next_power],
                                                                 dp[mask][last_power] + agents[i][next_power])

    # 최소 소멸 능력치 중에서 최솟값 찾기
    result = min(dp[(1 << n) - 1])

    # 갤럭시를 가동할 수 없는 경우
    if result == INF:
        return -1
    else:
        return result

# 테스트 케이스 수 입력
T = int(input())
for _ in range(T):
    # 최정예 요원 수 및 능력치 입력
    n = int(input())
    agents = [list(map(int, input().split())) for _ in range(n)]

    # 결과 출력
    print(min_destroyed_power(n, agents))
