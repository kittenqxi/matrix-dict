matrix=[[1, 5, 2], [8, 4, 7], [6, 8, 3]]
n=0
while n<len(matrix):
    n+=1
mx=matrix[0][0]
r=0
c=0
i=0
while i<n:
    m=0
    while m<len(matrix[i]):
        m+=1
    j=0
    while j<m:
        if matrix[i][j]>mx:
            mx=matrix[i][j]
            r=i
            c=j
        j+=1
    i+=1
print('Maximum:', mx)
print('Row:', r)
print('Colum:', c)