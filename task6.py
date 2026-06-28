matrix=[[1, 2, 3], [4, 5, 6]]
n=0
while n<len(matrix):
    n+=1
i=0
while i<n:
    m=0
    while m<len(matrix[i]):
        m+=1        
    left=0
    right=m-1
    while left<right:
        tmp=matrix[i][left]
        matrix[i][left]=matrix[i][right]
        matrix[i][right]=tmp
        left+=1
        right-=1
    i+=1
i=0
while i<n:
    m=0
    while m<len(matrix[i]):
        m+=1       
    j=0
    while j<m:
        print(matrix[i][j], end=" ")
        j+=1
    print()
    i+=1