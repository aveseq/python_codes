odds=[]
evens=[]
def check():
    for i in range(1,n+1):
        if i%2==0:
            evens.append(i)
        else:
            odds.append(i)
    
n=int(input("Enter non upto which u want to check: "))
check()
print("Odds: ",odds)
print("Evens: ",evens)