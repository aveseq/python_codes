n = int(input('Enter the no: '))
total = 0
excesv = 0
for i in range(1,n):
    if(n%i == 0):
        total = total+i
        if(total>n):
            excesv = 1
            break
if((total>n) or (excesv ==1)):
    print('It\'s an excessive no!' )
else:
    print('It\'s not an excessive no!' )
