"""ナップザックDP
"""

N, W = map(int, input().split())

v = []
w = []
for i in range(N):
    x, y = map(int, input().split())
    v.append(x)
    w.append(y)

dp = [[0] * (W + 1) for j in range(N + 1)]
print(dp)

for i in range(N):
    for j in range(W + 1):
        if j < w[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])
        print(dp)
print(dp[N][W])
