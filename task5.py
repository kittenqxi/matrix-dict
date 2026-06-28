matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n=0
while n<len(matrix):
    n+=1
maxs=0
firstr=0
while firstr<len(matrix[0]):
    firstr+=1
j=0
while j<firstr:
    maxs+=matrix[0][j]
    j+=1
max_idx=0
i=1
while i<n:
    m=0
    while m<len(matrix[i]):
        m+=1        
    rows=0
    j=0
    while j<m:
        rows+=matrix[i][j]
        j+=1      
    if rows>maxs:
        maxs=rows
        max_idx=i       
    i+=1
print(max_idx, maxs)