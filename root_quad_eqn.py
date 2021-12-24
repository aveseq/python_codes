import cmath
print('Enter the value of a,b & c from the given equation:')
a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))
d = (b**2)-(4*a*c)
if(d>=0):

    Root1 = (-b-cmath.sqrt(d))/(2*a)
    Root2 = (-b+cmath.sqrt(d))/(2*a)
    print('The required roots are:',Root1,' ',Root2)
else:
    print('Imaginary Roots!!')
