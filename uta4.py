#l = []
#for i in range(0,100,2):
#	if i%4==0:
#		l.append(i)
#print(l)
#print(l[len(l)-1])

#FILTER OUT THE ELEMENTS IN THE LIST L WHICH HAS "HELLO" IN IT AND APPEND IT'S POSITION TO A NEWW LIST AND PRINT THE NEW LIST
n = 5
l = ["hello","hi","hello",1,"hello"]
x = []
for i in range(len(l)): 
    if l[i]=="hello":
        x.append(i)
print(x) # TO PRINT THE ELEMENTS
for i in range(len(x)): #for i in x
    print(x[i],end=' ') #print(x, end=' ')

    
