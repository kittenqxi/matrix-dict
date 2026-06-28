matrix=[[1, 1, 1, 2, 3], [5, 5, 5, 5, 7], [8, 8, 2, 2, 2]]
n=0
while n<len(matrix):
    n+=1
a=0
i=0
while i<n:
    m=0
    while m<len(matrix[i]):
        m+=1
    if m>0:
        l=1
        j=1
        while j<m:
            if matrix[i][j]==matrix[i][j-1]:
                l+=1
            else:
                if l>a:
                    a=l
                a=1
            j+=1
        if l>a:
            a=l
    i+=1
print(a)