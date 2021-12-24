w=input()
d = dict()
for i in w:
    if i not in d:
        d.update({i:1})
    else: 
        d[i] = d[i]+1

keys = list(d.keys())
values = list(d.values())

index_of_max_val = values.index(max(values))
max_occured = keys[index_of_max_val]
print(max_occured)

count = 0
first_index_of_maxocc = w.find(max_occured)

for i in range(first_index_of_maxocc+1,len(w)):
    if w[first_index_of_maxocc] == w[i]:
        if count==0:
            print("No characters")
        elif count==1:
            print("1 character")
        else: print(f"{count} characters")
        count = 0
    else:
        count+=1
