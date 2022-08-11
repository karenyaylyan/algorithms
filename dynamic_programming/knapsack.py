W, n = map(int, input().split())
w = list(map(int, input().split()))

D = [[0]*(W + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, W + 1):
        D[i][j] = D[i - 1][j]
        if w[i - 1] <= j:
            D[i][j] = max(D[i][j], D[i-1][j-w[i - 1]] + w[i-1])

print(D[n][W])

