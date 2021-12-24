print("Enter the CGPA of a Student as M:")
M = float(input())
if (M>10):
    print('Invalid input!!')
else:
        if (10>=M>=9):
            print("Outstanding")
        if(9>M>=8):
            print('Excellent')
        if(8>M>=7):
            print('Good')
        if(7>M>=6):
            print('Average')
        if(6>M>=5):
            print('Better')
        if(M<5):
            print('Poor')


