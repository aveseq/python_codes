test=[]
for i in range(5):
    print("Enter test:",i," Min value:")
    min = float(input())
    print("Max value:")
    max = float(input())
    test.append((min,max))
for i in range(len(test)):
    print("The test range for test",i,"is:-",test[i])
test_type=int(input('Enter the test type(0-4): '))
obs_value=float(input('Enter the observation reading: '))
range_test=test[test_type]
min=range_test[0]
max=range_test[1]
print("Min is: ",min)
print("Max is: ",max)
if(min<obs_value<max):
    print("Your test is NORMAL for",obs_value)
else:
    print("Your test is ABNORMAL for",obs_value)
print("GOD BLESS")