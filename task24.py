gr= {'Anna': 7, 'Peter': 10, 'John': 9}
lst=list(gr.keys())
i=0
while i<len(lst):
    name=lst[i]
    gr[name]+=1
    if gr[name]>10:
        gr[name]=10
    i+=1
print(gr)