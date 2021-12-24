print('Enter the Marks')
M = int(input('Maths\' Marks '))
P = int(input('Physics\' Marks '))
C = int(input('Chemistry\'s Marks '))
tot_mark = (M + P + C)
avg = tot_mark/3;
if(M<0 or P<0 or C<0):
    print('Invalid input')
else:
    if(avg>=98):
        print('Graduate is eligible')
    else:
        print('Graduate is not eligible') 