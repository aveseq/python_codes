l=[1,1,2,3,5,6,1,2,3,2,2,3,3,3]
s=set(l)
#for i in s:
   # print(i,end=" ")
#l.sort()
#print(l)
l.append(23)
#print(l)
maximum=0
#for i in range(len(l)):
 #   if l[i]>maximum:
  #      maximum=l[i]
#print(maximum)
minimum=l[0]
for i in range(len(l)):
    if l[i]<maximum:
        maximum=l[i]
print(minimum)