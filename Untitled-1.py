a = "WELCOME TO VIT"
print(a)
print(len(a))
print(a.count(" "))
print(a.count(a[1]))
print(a[0:3])
l = list(a.split(" "))
l[-1] = "ALL"
str1 = " "
str1 = str1.join(l)
print(str1)
print(a+str1)
print(ord(a[0]))     #for ASCII Value
print(a.lower())     #TO lower case