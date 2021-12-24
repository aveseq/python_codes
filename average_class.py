i = 0
total = 0
n = int(input('Enter the no. of students: '))
while i<n:
    mark = float(input("Enter the marks of", i+1, "student:-"))
    if mark<0:
        print("Marks can't be negative!!")
        break
    total = total+mark
    i+=1
average = total/n
print('Average mark of students: ',average)
