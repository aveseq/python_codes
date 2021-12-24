group = []
n = int(input('Enter the size: '))
print('Enter no: ')
for i in range(0,n):
    num = int(input())
    group.append(num)
print('The group no.s are:', group)
a = int(input("Enter the no to find: "))
if(a == group):
       print("Found!!")
else:
       print("Not Found!!")