d={'cat':'кот', 'dog':'собака', 'mouse':'мышь'}
res={}
lst=list(d.keys())
i=0
while i<len(lst):
    k=lst[i]
    v=d[k]
    res[v]=k
    i+=1
print(res)