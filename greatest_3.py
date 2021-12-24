a=int(input("Enter the 1 no. "))
b=int(input("Enter the 2 no. "))
c=int(input("Enter the 3 no. "))
if (a>b) and (a>c):
    print(a,' is the greatest!!')
elif (b>a) and (b>c):
    print(b,' is the greatest!!')
elif (c>a) and (c>b):
    print(c,' is the greatest!!')
else:
    print('Any inputs are equal!!')
