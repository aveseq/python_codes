n=int(input('No. of terms:'))
l1=[]
for i in range(n):
    l1.append(l1[i])
    print(l1)
print(len(l1))
i=0
print('Enter character to find: ')
a=input()
for i in (0,n):
    if(a == l1[i]):
        print('Found')
    else:
        print('Not found')    
