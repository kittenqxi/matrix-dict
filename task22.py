text=input()
words=text.split()
res={}
i=0
while i<len(words):
    w=words[i]
    if w in res:
        res[w]+=1
    else:
        res[w]=1
    i+=1
lst=list(res.keys())
j=0
while j<len(lst):
    k=lst[j]
    print(k, ':', res[k])
    j+=1