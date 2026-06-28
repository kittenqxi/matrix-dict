pr={'Bread': 4, 'Milk': 7, 'Cheese': 15, 'Apples': 5}
p=float(input())
lst=list(pr.keys())
i=0
while i<len(lst):
    name=lst[i]
    if pr[name]<p:
        print(name)
    i+=1