A = input()
B = input()

n = len(A)
m = len(B)

D = [[0]*(m + 1) for i in range(n + 1)]


for i in range(n + 1):
    D[i][0] = i

for j in range(m + 1):
    D[0][j] = j

# for i in range(n + 1):
#     for j in range(m + 1):
#         print(D[i][j], end=' ')
#     print()



for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            c = 0
        else:
            c = 1

        D[i][j] = min(D[i][j-1] + 1, D[i-1][j] + 1, D[i-1][j-1] + c)
print(D[n][m])