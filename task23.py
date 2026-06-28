gr= {'Anna': 7, 'Peter': 10, 'John': 9}
lst=list(gr.keys())
bs=lst[0]
i=1
while i<len(lst):
    name=lst[i]
    if gr[name]>gr[bs]:
        bs=name
    i+=1
print(bs)