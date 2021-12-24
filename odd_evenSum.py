#i = 0
#while (i<=100):
 #   if i%2 ==0 and i%3 ==0:
  #      print(i)
   # i+=1

#for i in range(0,100,6):
#    print(i)
#PRINT SUM OF EVEN NO. & ODDS SEPARATELY 0-100
even_sum = 0
odd_sum = 0
for i in range(0,100):
    if i%2 == 0:
        even_sum+=i
    else:   
        odd_sum+=i
print(odd_sum , even_sum)
       