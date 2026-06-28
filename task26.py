dict1={'a':1, 'b':1}
dict2={'b':7, 'c':4}
res={}
lst1=list(dict1.keys())
i=0
while i<len(lst1):
    k=lst1[i]
    res[k]=dict1[k]
    i+=1
lst2=list(dict2.keys())
j=0
while j<len(lst2):
    k=lst2[j]
    res[k]=dict2[k]
    j+=1
print(res)