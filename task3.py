matrix=[[1, 2], [2, 1]]
n=0
while n<len(matrix):
    n+=1
sym=True
i=0
while i<n:
    j=0
    while j<n:
        if matrix[i][j]!=matrix[j][i]:
            sym=False
        j+=1
    i+=1
if sym:
    print('YES')
else:
    print('NO')