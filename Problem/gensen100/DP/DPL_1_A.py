n, m = map(int, input().split())
c = list(map(int, input().split()))

INF = 10 ** 6

dp = [[INF] * (n + 1) for _ in range(m + 1)]
dp[0][0] = 0

for i in range(m):
    for j in range(n + 1):
        if j < c[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = min(dp[i + 1][j - c[i]] + 1, dp[i][j])
#print(dp)
print(dp[m][n])
