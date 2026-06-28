matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n=0
while n<len(matrix):
    n+=1
m=0
while m<len(matrix):
    m+=1
j=0
while j<m:
    tmp=matrix[0][j]
    matrix[0][j]=matrix[n-1][j]
    matrix[n-1][j]=tmp
    j+=1
i=0
while i<n:
    rowm=0
    while rowm<len(matrix[i]):
        rowm+=1
    j=0
    while j<rowm:
        print(matrix[i][j], end=' ')
        j+=1
    print()
    i+=1