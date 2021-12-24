n = int(input('Enter any no. :'))
sum = 0
x = n
while x>0:
    digit = x%10
    sum+= digit**3
    x //= 10
if n == sum:
    print(n,'is an armstrong no!')
else:
    print(n,'is not an armstrong no!')