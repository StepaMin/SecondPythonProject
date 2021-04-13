def CreateSpiral():
    n = int(input())
    mat = [[0] * n for i in range(n)]
    currentValue, coef = 1, 0
    mat[n // 2][n // 2] = n * n
    for v in range(n//2):
        for i in range(n-coef):
            mat[v][i+v] = currentValue
            currentValue += 1
        for i in range(v+1, n-v):
            mat[i][-v-1] = currentValue
            currentValue += 1
        for i in range(v+1, n-v):
            mat[-v-1][-i-1] = currentValue
            currentValue += 1
        for i in range(v+1, n-(v+1)):
            mat[-i-1][v]=currentValue
            currentValue += 1
        coef += 2
    for i in mat:
        print(*i)

while(True):
    CreateSpiral()
