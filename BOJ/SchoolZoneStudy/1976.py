N = int(input())
M = int(input())
mat = []
for _ in range(N):
    row = list(map(int, input().split()))
    mat.append(row)
route = list(map(int, input().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                mat[i][j] = 1
                continue
            if mat[i][k] and mat[k][j]:
                mat[i][j] = 1
                mat[j][i] = 1

flag = True
for start in range(M-1):
    destination = start+1
    if not mat[route[start]-1][route[destination]-1]:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
