# 입력
T = 1  # 테스트 케이스 수
n = 4  # 최정예 요원의 수
agents = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
]

# 초기 설정
INF = float('inf')
dp = [[INF, INF, INF], [INF, INF, INF], [INF, INF, INF], [INF, INF, INF]]

for i in range(4):
    for j in range(3):
        dp[1 << i][j] = agents[i][j]

# 초기 dp 배열 출력
print("초기 dp 배열:")
for row in dp:
    print(row)

# 동적 계획법을 통한 최소 소멸 능력치 계산
for mask in range(1, 1 << 4):
    for last_power in range(3):
        if dp[mask][last_power] != INF:
            for i in range(4):
                if (mask & (1 << i)) == 0:
                    next_mask = mask | (1 << i)
                    for next_power in range(3):
                        if last_power != next_power:
                            dp[next_mask][next_power] = min(dp[next_mask][next_power],
                                                             dp[mask][last_power] + agents[i][next_power])

# 계산 후 dp 배열 출력
print("\n계산 후 dp 배열:")
for row in dp:
    print(row)

# 최종 결과 확인
result = min(dp[(1 << 4) - 1])
print("\n최종 결과:", result)

# 최종 결과 출력
if result == INF:
    print(-1)
else:
    print(result)
