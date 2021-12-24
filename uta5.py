l=[1,1,2,3,5,6,1,2,3,2,2,3,3,3]
distinct=[]
for i in range(len(l)):
    if l[i] not in distinct:
        distinct.append(l[i])
#print(distinct)
for i in distinct:
    print(i,end=" ")
for i in distinct:
    print('\n')
    print(i," - ",l.count(i))
